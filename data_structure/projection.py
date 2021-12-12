"""
source pillar = [1d,1w,1m,6m,1y,5y]
target_pillar = [1m,6m,2y]

"""
ref_pillar_to_days = {
    "1d":1,
    "1w":7,
    "1m":30,
    "6m":180,
    "1y":365,
    "2y":730,
    "5y":1825
}

def determine_target(source_pillars,target_pillars):
    source_pillars_days = [ref_pillar_to_days[x] for x in source_pillars]
    target_pillars_days = [ref_pillar_to_days[x] for x in target_pillars]
    return (source_pillars_days,target_pillars_days)


"""
    Step 1 - In the next step we join source pillar and target pillar and identify source pillar going to target pillar
    Step 2 - if a pillar is going to one target , coeff is 1 else coff is divided among two pillars based on distance ratio
    Step 3 - Once the ratio is generated, it is joined back to original pillars in the form (source pillar, (target_pillar, coeff))

    """


def generate_source_pillar_target_pillar_coeff(source_pillars_days, target_pillars_days):
    pairs = [[(x, y) for y in target_pillars_days] for x in source_pillars_days]
    list1 = []

    for x in pairs:
        prev = -1
        for (a, b) in x:
            if a < b:
                list1.append((a, b))
                break

            if a == b:
                if (b > prev and (a, prev) in list1):
                    list1.pop(list1.index((a, prev)))
                    list1.append((a, b))
                    break
                else:
                    list1.append((a, b))
                    break

            if a > b:
                if (b > prev and (a, prev) in list1):
                    list1.pop(list1.index((a, prev)))
                    list1.append((a, b))
                    prev = b
                else:
                    list1.append((a, b))
                    prev = b

    from collections import defaultdict
    reference_dict = defaultdict(list)

    for k, v in list1:
        reference_dict[k].append(v)

    list_pillar_coeff = []
    for x in reference_dict:
        coeff = []
        if len(reference_dict[x]) == 1:
            coeff.append(1)
            list_pillar_coeff.append((x, 1))
        else:
            two_pillars = reference_dict[x]
            denominator = two_pillars[1] - two_pillars[0]
            coeff1 = (x - two_pillars[0]) / denominator
            coeff2 = (two_pillars[1] - x) / denominator
            list_pillar_coeff.append((x, coeff1))
            list_pillar_coeff.append((x, coeff2))

    pairs_with_target = [(x, target_pillars[target_pillars_days.index(y)]) for (x, y) in list1]

    print(pairs_with_target)
    print(list_pillar_coeff)

    final_list = []

    for i in range(len(pairs_with_target)):
        (x, y) = pairs_with_target[i]
        (a, b) = list_pillar_coeff[i]
        final_list.append((source_pillars[source_pillars_days.index(x)], (y, b)))

    return final_list


if __name__=="__main__":

    source_pillars = ["1d", "1w", "1m", "6m", "1y", "5y"]
    target_pillars = ["1m", "6m", "2y"]
    """convert source and target pillars to days 
    source_pillars_days =  [1, 7, 30, 180, 365, 1825]
    target_pillars_days = [30, 180, 730]
    
    """
    source_pillars_days,target_pillars_days = determine_target(source_pillars, target_pillars)

    final_list = generate_source_pillar_target_pillar_coeff(source_pillars_days,target_pillars_days)
    print(final_list)





