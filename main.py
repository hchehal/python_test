def in_autotests_we_trust(a, b):
    if a == b:
        print('PASS')
    else:
        print('FAIL')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)def in_autotests_we_trust(a, b):
    if a == b:
        print('Test passed')
    else:
        print('Test failed')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
