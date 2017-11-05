def main():
    country = "United stats of India"
    state = "Ohio"
    name = '1st'
    print (u"im the {name} largest country in world") #u - unicode

    print(f"im the {} largest country in world".format('1st'))#

    print(r"im the {} largest country in world".format('1st')) #r is raw
   # print("im the {} largest country in world".format('1st'))
    state_short = state[:2].upper()
    print (state_short)


    if "India" in country:
        print("Yes, the word \"India\" is in {0:*^29}".format(country))

main()