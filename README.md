# 🐍 Snake Xenzia — Classic Snake Game in Python

## 🎯 Short Description

A modern recreation of the classic **Snake Xenzia** game built using Python and the `turtle` graphics library. The goal is simple: **Eat. Grow. Survive.**  
This game offers smooth movement, collision detection, and a responsive score tracker — all coded from scratch.

---

## ⚙️ Tech Stack Used

- **Language:** Python 3  
- **Library:** `turtle` (for graphics)  
- **Concepts:** OOP, game loop, collision detection, modular design

---

## 🚀 Features

- ✅ Real-time snake movement with keyboard input  
- ✅ Collision detection with food, wall, and self  
- ✅ Live score display  
- ✅ Game Over screen  
- ✅ Clean, modular code across multiple Python files

---

## 💻 How to Run the Game

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/snake-xenzia-python.git
   cd snake-xenzia-python
````

2. **Run the game**

   ```bash
   python main.py
   ```

> ⚠️ Make sure you have Python 3 installed. This game uses the built-in `turtle` module, so no extra installations needed.

---

## 📸 Screenshots

> *(Add a GIF or screenshot here of the gameplay — consider using screen recording tools like ShareX, OBS Studio, or LICEcap.)*

---

## 🧠 Key Learnings & Challenges

* Mastered **object-oriented programming** by separating logic into `Snake`, `Food`, and `ScoreBoard` classes.
* Learned how to manage **real-time input** and **frame-by-frame updates** using `Screen.tracer()` and `Screen.update()`.
* Implemented **basic game architecture** including event listeners and collision logic.
* Faced and overcame issues like **body collision detection** and **screen boundary management**.

---

## 🔮 Future Improvements

* Add difficulty levels or game speed increase over time
* Add sound effects and background music
* Store high scores locally
* Add start/pause menu and animations
* Improve UI with custom sprites instead of turtle shapes

---

## 📁 Project Structure

```
/snake-xenzia-python
├── main.py             # Main game loop
├── snake.py            # Snake movement and behavior
├── food.py             # Food creation and placement
├── Scoreboard.py       # Score tracking and Game Over message
├── README.md           # You're here!
├── LICENSE             # MIT License
└── .gitignore          # Python & system ignores
```

---
Made with ❤️ by **Hari**
