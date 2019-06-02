package com.example.demorsocketrpc;

import io.rsocket.RSocketFactory;
import io.rsocket.transport.netty.client.TcpClientTransport;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.time.Duration;
import java.util.concurrent.CountDownLatch;

public class DemoClient {

    public static void main(String[] args) throws Exception {
//        bidirection_stream_test();
    request_reply_test();
    }

    // in rsocket term, bidirectional stream is called channel
    public static void bidirection_stream_test() throws InterruptedException {
        SimpleServiceClient client = RSocketFactory.connect()
                .transport(TcpClientTransport.create(8801))
                .start()
                .map(SimpleServiceClient::new)
                .block();

        CountDownLatch latch = new CountDownLatch(1);
        Flux<SimpleRequest> request = Flux.interval(Duration.ofSeconds(1))
                .take(10)
                .map(i -> SimpleRequest.newBuilder().setRequestMessage("hi" + i).build());
        Flux<SimpleResponse> response = client.streamingRequestAndResponse(request)
                .log()
                .doFinally(x -> latch.countDown());
        response.subscribe();
        latch.await();
    }

    public static void request_reply_test() {
        System.out.println("request reply test");
        SimpleRequest request = SimpleRequest.newBuilder().setRequestMessage("Aloha ").build();
        SimpleServiceClient client = RSocketFactory.connect()
                .transport(TcpClientTransport.create(8801))
                .start()
                .map(SimpleServiceClient::new)
                .block();

        Mono<SimpleResponse> response =
                client.requestReply(request).doOnNext(r -> System.out.println(r.getResponseMessage()));

        System.out.println(response.toString());

    }
}
