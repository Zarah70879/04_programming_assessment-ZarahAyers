# V1 of Budget Calculator Final Program


# Not Blank function goes here
def not_blank(question, error_msg, ):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)

        # If response is blank, question is repeated (loop starts over)
        if response == "":
            print(error)
            continue

        # if response is not blank, program continues
        else:
            return response


# Number Checking Function goes here
def num_check(question):
    error = "Please enter a number that is more than zero"
    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:

                print(error)
            else:
                return response
        except ValueError:

            print(error)


# main routine

# set up lists
printout = []
kg_weight = []
afford_list = []
weight_aff = []
tp_weight = []

# Bold print out text option
bold = "\033[1m"
reset = "\033[0;0m"

# introduce the user to the program
print(bold, "Budget Calculator", reset)
print("This program is used to compare prices of products in store")
print("The program will then remove the items you can't afford and "
      "suggest one of the products based on its cost and weight.")
print()

# Ask user what their budget is for the item
budget = num_check("What is your budget: $")
print()

# loop of getting information from user
print("Please enter a product, its cost and its weight.")
print("If you have finished entering products type", bold, "'exit'", reset,
      "to get a printout of the products")
print()

stop = ""
while stop != "exit":
    product = []
    print()
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'exit' to quit").lower()
    product.append(get_product)

    # if user enters exit code break loop
    if get_product == "exit":
        break

    # get cost from user
    get_cost = num_check("Cost: $")

    # get weight of item from user
    get_weight = num_check("Weight(g): ")

    # append the information the user entered into a single line of code
    # if the weight is in g:
    if get_weight > 0.999:
        printout.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight))
        kg_weight.append(get_weight / 1000)

    # if weight is in kg already:
    else:
        printout.append("${:.2f} {}, {}kg".format(get_cost, get_product.title(), get_weight))
        kg_weight.append(get_weight)

    # if the user can afford the product
    if budget == get_cost:
        afford_list.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight))
        weight_aff.append(get_weight)

        # get the suggested item
        tp_weight = ("${:.2f} {}, {}g".format(get_cost, get_product.title(), max(weight_aff)))

    elif budget > get_cost:
        afford_list.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight))
        weight_aff.append(get_weight)

        # get the suggested item
        tp_weight = ("${:.2f} {}, {}g".format(get_cost, get_product.title(), max(weight_aff)))


# print out list of items
print()
print(bold, "Items: ", reset)
for item in printout:
    print(item)

# print out items they can afford
print()
if afford_list != []:
    print(bold, "Affordable product/s within a ${:.2f} budget: ".format(budget), reset)
    for item in afford_list:
        print(item)

    # print out the suggested item
    print()
    print(bold, "Suggested Item:", reset)
    print(tp_weight)
else:
    print("--------------------------------------")
    print("You can't afford any of these products")
    print("--------------------------------------")
