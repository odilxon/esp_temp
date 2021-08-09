import pandas as pd



def Check(hand, base):
    total = 0

  

    count = 8 
    return total/count * 100



def Read():
    hand = pd.read_excel('hand.xlsx')
    base = pd.read_excel('base.xlsx')
    for row_id, row_data in hand.iterrows():
        biggest = {"percent" : 0, "data" : ""}
        for b_row_id, b_row_data in base.iterrows():
            percent = Check(row_data, b_row_data)
            if biggest['percent'] < percent :
                biggest['percent'] = percent
                biggest['data'] = b_row_data

        hand['person_EduERP_id'][row_id] = biggest['data'][0]
        hand['percent'][row_id] = biggest['percent']

        
        
        break
    with pd.ExcelWriter('output.xlsx') as writer:
        hand.to_excel(writer)

Read()