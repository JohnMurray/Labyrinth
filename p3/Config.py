#Authors: Brad Stephens, John Murray
#Configuration File

weapon = {} 
sword = {} 
sword["min_min"] = ( 1, 1, 7 )
sword["abs_min"] = ( 3, 3, 7 ) 
sword["chance_min"] = ( 0, 0, 5 )
sword["abs_range"] = ( 21, 33, 33 )
sword["min_range"] = ( 12, 21, 21 )
sword["chance_range"] = ( 5, 10, 10 )
weapon["sword"] = sword
hammer = {} 
hammer["min_min"] = ( 10, 10, 18 )
hammer["abs_min"] = ( 5, 5, 10 )
hammer["chance_min"] = ( 0, 0, 1 )
hammer["abs_range"] = ( 31, 41, 41 )
hammer["min_range"] = ( 22, 30, 30 )
hammer["chance_range"] = ( 3, 6, 6 )
weapon["hammer"] = hammer
spear = {}
spear["min_min"] = ( 5, 5, 11, )
spear["abs_min"] = ( 3, 3, 9, ) 
spear["chance_min"] = ( 0, 0, 2, )
spear["abs_range"] = ( 21, 33, 33, )
spear["min_range"] = (  16, 25, 25, )
spear["chance_range"] = ( 4, 8, 8, )
weapon["spear"] = spear
arrow = {}
arrow["min_min"] = ( 12, 12, 22, )
arrow["abs_min"] = ( 5, 5, 10, )
arrow["chance_min"] = ( 0, 0, 1, )
arrow["abs_range"] = ( 26, 36, 36, ) 
arrow["min_range"] = ( 25, 35, 35, ) 
arrow["chance_range"] = ( 3, 6, 6, ) 
weapon["arrow"] = arrow

item = {
    'spell': {
        'attack': {
            'common': (1, 3, 1, 3),
            'normal': (2, 4, 2, 4),
            'rare': (),
        },
        'defense': {
            'common': (1, 3, 1, 3, 1, 3),
            'normal': (2, 4, 2, 4, 2, 4),
            'rare': (4, 6, 4, 6, 4, 6),
        },
        'stun': {
            'common': (1, 3, 1, 3),
            'normal': (2, 4, 2, 4),
            'rare': (4, 6, 4, 6),
        },
    },
    'potion': {
        'magic_ofense': {
            'common': (1, 3, 1, 3),
            'normal': (1, 5, 3, 6),
            'rare': (3, 7, 4, 8),
        },
        'magic_defense': {
            'common': (1, 3, 1, 3),
            'normal': (3, 5, 2, 5),
            'rare': (4, 6, 3, 7),
        },
        'healing': {
            'common': (, 20, 30),
            'normal': (80, 100),
            'rare': (160, 200),
        },
        'defense': {
            'common': (1, 3, 1, 3),
            'normal': (1, 5, 3, 5),
            'rare': (3, 7, 4, 6),
        },
        'offense': {
            'common': (1, 3, 2, 5),
            'normal': (1, 6, 3, 6),
            'rare': (3, 7, 5, 11),
        },
    },
}
