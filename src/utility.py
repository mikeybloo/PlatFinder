def itemToSlug(itemName):
    itemName = itemName.lower()
    slug = itemName.replace(" ", "_")

    return slug