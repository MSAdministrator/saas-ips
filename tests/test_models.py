
def test_models():
    from src.saas_ips.models import KnownIPs, Source, Service, IP

    known = KnownIPs(
        sources=[
            Source(
                name="test",
                url="https://letsautomate.it",
                services=[
                    Service(
                        name="test_service",
                        ips=[
                            IP(
                                ip="123.123.123.123",
                                region="china"
                            )
                        ]
                    )
                ]
            )
        ]
    )

    assert known.last_updated != None
    assert len(known.sources) == 1
    assert len(known.sources[0].services) == 1

    known.sources[0].add_service(
        name="source2",
        ips="8.8.8.8",
        region="US"
    )
    assert len(known.sources[0].services) == 2
