"""Examples of dictionary syntax with Icre Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
# len evaluates to the number of entries
print(len(ice_cream))  # Prints 3

# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3

# accesss entries by their key
print(ice_cream["chocolate"])  # Prints 12

# test if "pbj" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream

# to remove, we use the pop method and give a key
ice_cream.pop("strawberry")

# to iterate over every key in a loop, use for in
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
