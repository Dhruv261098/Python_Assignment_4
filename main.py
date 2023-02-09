#Dhruv Desai
#c0883865

# 3-4
invitation_list = ["Manav", "OM", "Jenish"]
print(invitation_list[0], "Join us for dinner today night at 9:00")
print(invitation_list[1], "Join us for dinner today night at 9:00")
print(invitation_list[2], "Join us for dinner today night at 9:00\n")

# 3-5
print("Manav could not able to join us!! \n")
invitation_list[0] = "Aditya"
print(invitation_list[0], "Be ready to join us for dinner today night at 9:00")
print(invitation_list[1], "Be ready to join us for dinner today night at 9:00")
print(invitation_list[2], "Be ready to join us for dinner today night at 9:00\n")

# 3-6
print("Hey guys guess what I found bigger table so we can invite 3 more people to join us!!!\n")

invitation_list.insert(0,"Ansu")
invitation_list.insert(2, "Montu")
invitation_list.append("Ashwin")

print(invitation_list[0], "Hurray!! We are meeting for dinner")
print(invitation_list[1], "Hurray!! We are meeting for dinner")
print(invitation_list[2], "Hurray!! We are meeting for dinner")
print(invitation_list[3], "Hurray!! We are meeting for dinner")
print(invitation_list[4], "Hurray!! We are meeting for dinner")
print(invitation_list[5], "Hurray!! We are meeting for dinner\n")

# 3-7
print("Hey guys really sorry but I could only invite two people because the table I booked won't arrive!!\n")

print(invitation_list.pop(), ", I'm really sorry for not inviting you for dinner!!")
print(invitation_list.pop(), ", I'm really sorry for not inviting you for dinner!!")
print(invitation_list.pop(), ", I'm really sorry for not inviting you for dinner!!")
print(invitation_list.pop(), ", I'm really sorry for not inviting you for dinner!!\n")

print(invitation_list[0], "You are still in my list, We will meet soon!")
print(invitation_list[1], "You are still in my list, We will meet soon!\n")

del invitation_list[0:2]

print("I'm alone now!!", invitation_list, "\n")


# 3-8
places_list = ["Goa", "Maldives", "Singapore", "New York", "Paris"]
print("Original List", places_list)
print(sorted(places_list))
print("Original List",places_list)
print(sorted(places_list, reverse=True))
print("Original List",places_list)
places_list.reverse()
print(places_list)
places_list.reverse()
print(places_list)
places_list.sort()
print(places_list)
places_list.sort(reverse=True)
print(places_list)

# 3-9
invitation_list = ["Manav", "OM", "Jenish"]
print("\n Total invited people for dinner are: ", len(invitation_list))

# 3-10
countries_list = ["India", "Canada", "USA", "China"]
print(countries_list)
print(countries_list.pop())
print(sorted(countries_list))
countries_list.append("Thailand")
print(countries_list)
print(countries_list.count("India"))
print(countries_list.index("USA"))
countries_list.remove("USA")
print(countries_list)
countries_list.insert(0,"Africa")
print(countries_list)
countries_list.reverse()
print(countries_list)
countries_list.sort()
print(countries_list)
countries_list.clear()
print(countries_list)