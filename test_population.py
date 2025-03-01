from population import population

def test_population():
    assert population(1) == 3  # 1 man, 1 woman, 1 child -> 3 total
    assert population(2) == 14  # 2 men, 4 women, 8 children -> 14 total
    assert population(3) == 39  # 3 men, 9 women, 27 children -> 39 total
    assert population(0) == 0  # No men, no population
    assert population(4) == 84  # 4 men, 16 women, 64 children -> 84 total