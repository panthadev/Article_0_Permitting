import matplotlib.pyplot as plt
import pandas as pd

#--------graph1-----------

df = pd.read_csv("Goleta_Zoning_Permits.csv")

df["Name"] = df["First Name"].str.capitalize() + " " + df["Last Name"].str.capitalize()

count = df["Name"].value_counts().sort_values() #56 people
print(type(count))

bar_height = 0.7
bar_color = "#307473"

fig, ax = plt.subplots()

graph1 = plt.barh(count.index, count.values, height=bar_height, color=bar_color, align='edge')
# #
plt.title("Top ten people who have requested a permit")
plt.xlabel("Permits Requested")
plt.ylabel("people")

plt.xticks(fontsize = 6)
plt.yticks(fontsize = 10)
# plt.tick_params(labelleft=False)
plt.ylim(len(count) - 10, len(count)) #top 10
# #
count_topten = count[46:56:][:]
name_dict = dict(count_topten)
# #
# ax.bar_label(count_topten.item)
 # plt.text(0.3, 20, "Lonnei Roy", fontsize = 10)

# for name in name_dict:
#     print(name)
 #     x_pos = 20
#     y_pos = 0 #starting
#     plt.text(x_pos, name, name, fontsize = 10)
#     y_pos += bar_height

#--------graph2-----------

organization = df["Organization Name"].value_counts().sort_values()
print(organization)

graph2 = plt.barh(organization.index, organization.values, height=bar_height, color=bar_color, align='edge')

plt.show()