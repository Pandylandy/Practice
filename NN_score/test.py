from pickle import load, dump
import random
from CGRtools.files import SDFwrite
from CGRtools.files import SDFread


global_result = set()
pairs, SIG = set(), set()
NUMBER, NUMBER2, NUMBER3 = set(), set(), set()
train, test, validation = set(), set(), set()


end = False
for numeric in range(0, 43492):
    tuples = load(open('/home/nadia/data/True_pairs_new/{}.pickle'.format(numeric), 'rb'))
    for take_ml in tuples:
        a = take_ml[0]
        b = take_ml[1]
        sig_a = bytes(a)
        sig_b = bytes(b)
        if (sig_b, sig_a) in pairs or (sig_a, sig_b) in pairs:
            continue
        TUPLE = (sig_a, sig_b, take_ml[2], take_ml[3])
        pairs.add((sig_a, sig_b))
        check_a = ([t[0] for t in global_result])
        check_b = ([t[1] for t in global_result])
        if sig_b in check_b or sig_b in check_a:
            train.add(take_ml)
        else:
            if len(test)*8 > len(train):
                train.add(take_ml)
            elif len(validation) < len(test):
                validation.add(take_ml)
            else:
                test.add(take_ml)
        global_result.add(TUPLE)
        if len(train) == 16000:
            NUMBER3.add(max(NUMBER3)+1)
            with open('/home/nadia/data/train/{}train_copy.pickle'.format(max(NUMBER3)+1)) as f:
                dump(train[7999:], f)
        if numeric == 43491 and take_ml == tuples[-1]:
            end = True
        if len(validation) == 1000 or end:
            NUMBER.add(max(NUMBER)+1)
            with open('/home/nadia/data/validation/{}validation.pickle'.format(max(NUMBER)+1)) as f:
                dump(validation, f)
            validation.clear()

            NUMBER2.add(max(NUMBER2)+1)
            with open('/home/nadia/data/test/{}test.pickle'.format(max(NUMBER2)+1)) as f:
                dump(test, f)
            test.clear()
            NUMBER3.add(max(NUMBER3)+1)
            with open('/home/nadia/data/train/{}train.pickle'.format(max(NUMBER3)+1)) as f:
                dump(train, f)
            train.clear()



