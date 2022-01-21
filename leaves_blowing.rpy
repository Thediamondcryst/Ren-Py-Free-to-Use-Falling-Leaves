# image leaves_blowing:
    # Fixed(SnowBlossom(Animation("images/sans_leaf.png", 0.15, "images/papyrus_leaf.png", 0.15), count=50, xspeed=(200, 20),horizontal=True))

transform featherspin:
    xpos 0.5
    ypos 0.5
    linear 3 rotate 360 # take 1 second to rotate 360 degrees
    rotate 0 # reset position counter
    repeat

# Oak
image oak_leaves_blowing_low_wind:
    SnowBlossom(At("images/leaves/oak_leaf.png", featherspin), count=50, xspeed=(200, 20),horizontal=True)    

image oak_leaves_blowing:
    SnowBlossom(At("images/leaves/oak_leaf.png", featherspin), count=100, xspeed=(200, 20),horizontal=True)

image oak_leaves_blowing_high_wind:
    SnowBlossom(At("images/leaves/oak_leaf.png", featherspin), count=150, xspeed=(600, 20),horizontal=True)


# Maple
image maple_leaves_blowing_low_wind:
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=50, xspeed=(200, 20),horizontal=True)

image maple_leaves_blowing:
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=100, xspeed=(200, 20),horizontal=True)

image maple_leaves_blowing_high_wind:
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=150, xspeed=(600, 20),horizontal=True)

image maple_leaves_blowing_autumn = Fixed(
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=40, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/red_maple_leaf.png", featherspin), count=20, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/orange_maple_leaf.png", featherspin), count=20, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/yellow_maple_leaf.png", featherspin), count=20, xspeed=(200, 20),horizontal=True),
    )

image maple_leaves_blowing_autumn_low_wind = Fixed(
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=20, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/red_maple_leaf.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/orange_maple_leaf.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/yellow_maple_leaf.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    )

image maple_leaves_blowing_autumn_high_wind = Fixed(
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=60, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/red_maple_leaf.png", featherspin), count=30, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/orange_maple_leaf.png", featherspin), count=30, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/yellow_maple_leaf.png", featherspin), count=30, xspeed=(600, 20),horizontal=True),
    )


# Birch
image birch_leaves_blowing_low_wind:
    SnowBlossom(At("images/leaves/birch_leaf.png", featherspin), count=50, xspeed=(200, 20),horizontal=True)

image birch_leaves_blowing:
    SnowBlossom(At("images/leaves/birch_leaf.png", featherspin), count=100, xspeed=(200, 20),horizontal=True)

image birch_leaves_blowing_high_wind:
    SnowBlossom(At("images/leaves/birch_leaf.png", featherspin), count=150, xspeed=(600, 20),horizontal=True)


# Cherry Blossom
image cherry_blossom_leaves_blowing = Fixed(
    SnowBlossom(At("images/leaves/cherry_blossom_leaf.png", featherspin), count=90, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf_big.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    )

image cherry_blossom_leaves_blowing_low_wind = Fixed(
    SnowBlossom(At("images/leaves/cherry_blossom_leaf.png", featherspin), count=45, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf_big.png", featherspin), count=5, xspeed=(200, 20),horizontal=True),
    )

image cherry_blossom_leaves_blowing_high_wind = Fixed(
    SnowBlossom(At("images/leaves/cherry_blossom_leaf.png", featherspin), count=125, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf_big.png", featherspin), count=25, xspeed=(600, 20),horizontal=True),
    )


# Any
image leaves_blowing = Fixed(
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=30, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/birch_leaf.png", featherspin), count=20, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/oak_leaf.png", featherspin), count=20, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf.png", featherspin), count=20, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf_big.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    )

image leaves_blowing_low_wind = Fixed(
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=15, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/birch_leaf.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/oak_leaf.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf.png", featherspin), count=10, xspeed=(200, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf_big.png", featherspin), count=5, xspeed=(200, 20),horizontal=True),
    )

image leaves_blowing_high_wind = Fixed(
    SnowBlossom(At("images/leaves/maple_leaf.png", featherspin), count=45, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/birch_leaf.png", featherspin), count=30, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/oak_leaf.png", featherspin), count=30, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf.png", featherspin), count=30, xspeed=(600, 20),horizontal=True),
    SnowBlossom(At("images/leaves/cherry_blossom_leaf_big.png", featherspin), count=15, xspeed=(600, 20),horizontal=True),
    )