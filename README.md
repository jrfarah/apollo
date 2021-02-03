# Apollo PRERELEASE EXPERIMENTATION REPO
## Description: Wrapper for sklearn

IF YOU ARE LOOKING TO INSTALL `apollo` YOU'VE COME TO THE WRONG PLACE. SEE `apollo_prod` or install with `pip`:

`pip install apollo_ml`

Features
- Reduces sklearn classification code from 150 lines to 2 lines

Currently working on:
- turning classification procedures into rudimentary prediction ones

Download this repo if you want to see whatever crazy crap I'm working on. I can't guarantee everything in here will work, but I can guarantee it will be fun! 

- Note: you can't import the code in here the way you would normally import Apollo. See `FormulaicImplementation.py` for an example of how to access `core`. 

## Structure of this repo:
- `prep`: my sandbox. I'm fiddling around with algorithms, testing out sklearn features, messing with pandas. This will definitely not in apollo_prod, but methods I write in here will usually find its way into the main library.

- `src`: Contains the important stuff
 - `core`: the modules. Most of this stuff will be in Apollo releases. 
 - `interface`: where I test stuff out, implement things. If I write a GUI it will probably go in here.

- `training_sets`: csvs and .datas that the `interface` folder accesses. 
