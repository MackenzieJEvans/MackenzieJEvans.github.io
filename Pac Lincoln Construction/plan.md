# Cone Zone: Lincoln — Project Plan

A browser maze game about road construction in Lincoln, Nebraska. The player drives through a stylized downtown street grid, collects fuel, avoids traffic cones, and detours around closed roads.

**Live page:** https://mackenziejevans.github.io/Pac%20Lincoln%20Construction/
**Source:** `Pac Lincoln Construction/index.html` (a single self-contained file)

---

## 1. Purpose

- Show the detours that students, truck drivers and other people have to take to reach campus while Lincoln streets are under construction.
- Tie the game to reporting. The description links to the Daily Nebraskan story [O Street road closure forces UNL students to adjust to new routes](https://www.dailynebraskan.com/news/o-street-road-closure-forces-unl-students-to-adjust-to-new-routes/article_85f38951-9f6f-45ba-bf72-c234501b9c1c.html).
- Serve as a portfolio piece, alongside the Election Count Up trivia game.

## 2. Core gameplay

| Element | How it works |
|---|---|
| Goal | Collect every yellow fuel drop to clear the level. Each new level brings faster cones. |
| Fuel bar (replaces lives) | Fuel starts at 100% and drains over time, at a rate set by the vehicle. When it reaches 0, the game is over. |
| Fuel drops | +0.6 fuel and 10 points each. |
| Gas stations (4, one in each corner area) | +40 fuel and 50 points, and every cone is knocked over for a few seconds. |
| Knocked-over cones | Drive through them for 200 / 400 / 800 / 1600 points in a row. A plowed cone goes back to the Cone Yard. |
| Cone hit | Costs fuel (amount depends on the vehicle) and gives 2 seconds of protection from further hits. |
| Level clear | +25 fuel bonus, then the next level with faster cones that leave the yard sooner. |
| High score | Saved in the player's own browser. |

## 3. Vehicles

| Vehicle | Speed (tiles/s) | Fuel drain/s | Damage per hit | Special |
|---|---|---|---|---|
| Fire Truck | 6.6 | 2.3 | 22 | **Space** turns on the siren and lights for 4.5 s: cones pull over and can be plowed. 14 s cooldown, extra fuel burn while it's on. |
| Tractor | 3.4 | 1.1 | 12 | Very slow, but sturdy. Cones also move slower against it (78% speed). |
| Sedan | 5.0 | 0.8 | 25 | Average speed, best fuel economy. |
| Semi Truck | 4.6 | 3.3 | 28 | Gets stuck: pauses on turns, needs a 3-point turn to reverse, sometimes stalls at intersections, and gets stuck when hit. |
| Fuel Truck | 4.4 | refuels +0.7/s | — | Refuels itself while driving, but explodes on its first cone hit (instant game over). Does **not** get stuck. |

## 4. The map

- A 24 × 27 tile grid styled after a dark traffic map. Road lines change color with how close the cones are: green when clear, yellow when a cone is near, red when one is very close.
- Street names follow downtown Lincoln: **9th–16th St** run north–south, **J–R St** run east–west. It is stylized and not to scale.
- Landmarks: Pinnacle Bank Arena and the Haymarket (top left), Memorial Stadium (top right), the State Capitol (bottom center).
- **Cone Yard** in the middle: cones start here and leave one at a time through a gate that only cones can use.
- **Road closed** tiles (orange striped barricades) are permanent walls for both the player and the cones. They are final as designed and should not be changed.
- **O Street** runs off both edges of the map and wraps around as a shortcut.

## 5. Cones

There are four cone types. Each chases the player a different way:

1. **Traffic cone** heads straight for the player.
2. **Orange barrel** aims a few tiles ahead of the player.
3. **Barricade** chases from a distance and backs off when close.
4. **Work sign** tries to cut the player off, working with the traffic cone.

Every 25 seconds the cones spend about 5 seconds heading back to their corners, which gives the player room to breathe.

## 6. Branding

The page uses Daily Nebraskan styling to match the Election Count Up game:

- Gray topbar, serif "Daily Nebraskan" wordmark, and a "Games & Puzzles" tag.
- A dark section bar with **Games** underlined in red.
- A red block title, Open Sans body text, and Roboto Condensed headings.
- DN red (`#ba1f1f`) for buttons and accents, with a white page.
- The game board keeps its dark traffic-map look so it stands out on the page.

**To confirm:** the Daily Nebraskan is fine with its name and masthead appearing on a personal portfolio page.

## 7. Controls

- **Keyboard:** arrow keys or WASD to steer, Space for the siren (fire truck only), P or Esc to pause, M to mute. On the vehicle screen, keys 1–5 pick a vehicle and Enter starts.
- **Phones:** swipe on the map or use the on-screen arrow pad. A siren button appears for the fire truck.
- The game pauses automatically when the player switches away from the browser tab.

## 8. Technical notes

- One HTML file with inline CSS and JavaScript. It draws the game on a canvas and needs no build step or libraries. Fonts load from Google Fonts.
- The street map is a block of text in the script (`MAP`). Each character is one tile: `#` block, `.` road with fuel, `G` gas station, `S` start, `T` O Street edge, `X` road closed, `p` Cone Yard, `-` yard gate.
- Movement is tile-based, so turns can be pressed early and happen at the next intersection.
- Sound effects are generated in the browser, with no audio files.
- `window.__cz` is a small testing hook left in the script. It is harmless, but can be removed before final publishing.

## 9. Status

**Done and live on GitHub:**
- [x] Maze, fuel bar, cones, gas stations, level progression
- [x] Five vehicles, including the fire truck siren and fuel truck explosion
- [x] Road closures as permanent barriers
- [x] Description and Daily Nebraskan article link
- [x] Fuel truck no longer gets stuck (semi only)
- [x] Daily Nebraskan branding
- [x] Portfolio back link removed

**Not done yet:**
- [ ] Play-test every vehicle by hand and tune difficulty (the game logic was checked with scripts, not by a person playing)
- [ ] Check the layout on a real phone
- [ ] Decide whether to link the game from the portfolio home page
- [ ] Consider renaming the folder (for example `cone-zone`) so the web address has no `%20`
- [ ] Remove the `window.__cz` testing hook

## 10. Ideas for later

- Real closures from the reporting, such as specific O Street blocks, shown as labeled closures on the map.
- A short "road report" ticker with facts or quotes from the Daily Nebraskan story.
- Rush-hour levels with more cones and slower traffic.
- A shared leaderboard instead of a high score saved per browser.
