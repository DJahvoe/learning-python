coffee_machine_is_on = True

coffee_requirements = {
    "espresso": {
        "label": "Espresso",
        "price": 1.5,
        "required_amount": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        }
    },
    "latte": {
        "label": "Latte",
        "price": 2.5,
        "required_amount": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        }
    },
    "cappuccino": {
        "label": "Cappuccino",
        "price": 3.0,
        "required_amount": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        }
    }
}

# water in mililiters
# milk in mililiters
# coffee in grams
# money in $
coffee_machine_resources = {
    "water": {
        "label": "Water",
        "amount": 500,
        "unit": "ml"
    },
    "milk": {
        "label": "Milk",
        "amount": 200,
        "unit": "ml"
    },
    "coffee": {
        "label": "Coffee",
        "amount": 100,
        "unit": "gr"
    },
    "money": {
        "label": "Money",
        "amount": 0,
        "unit": "$"
    }
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

while coffee_machine_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    match user_input:
        case "off":
            print("Coffee Machine Turned Off..")
            break
        case "report":
            for _, resource in coffee_machine_resources.items():
                print(f"{resource['label']}: {resource['amount']}{resource['unit']}")
        case "espresso" | "latte" | "cappuccino":
            # Select coffee
            chosen_coffee = coffee_requirements[user_input]

            # Check requirements
            requirement_is_met = True
            required_amount = chosen_coffee["required_amount"]
            for name, requirement in required_amount.items():
                if coffee_machine_resources[name]["amount"] < requirement:
                    print(f"Sorry there is not enough {name}.")
                    requirement_is_met = False
                    break
            if not requirement_is_met:
                continue


            price = chosen_coffee["price"]
            # Insert coins
            inserted_sum = 0
            inserted_sum += int(input("Inserted quarters: ")) * coins["quarters"]
            inserted_sum += int(input("Inserted dimes: ")) * coins["dimes"]
            inserted_sum += int(input("Inserted nickles: ")) * coins["nickles"]
            inserted_sum += int(input("Inserted pennies: ")) * coins["pennies"]
            
            # Rounded change into 2 decimal places
            change = round(inserted_sum - price, 2)
            if change > 0:
                print(f"Here is ${change} dollars in change.")
            elif change < 0:
                print("Sorry that's not enough money. Money refunded.")
                continue
            
            # Process Coffee
            required_amount = chosen_coffee["required_amount"]
            for name, requirement in required_amount.items():
                coffee_machine_resources[name]["amount"] -= requirement
            coffee_machine_resources["money"]["amount"] += price
            print(f"Here is your {chosen_coffee["label"]}. Enjoy!")
            
                
            
                


        