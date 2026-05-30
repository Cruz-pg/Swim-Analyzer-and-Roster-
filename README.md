# SwimCoach AI

An AI-powered swim coaching web app — no installation required. Runs entirely in the browser from a single HTML file.

---

## What It Does

### Video / Image Analysis
Upload a swim photo or video clip and get AI feedback on technique. The coach evaluates based on stroke-specific checkpoints:

- **Freestyle** — hand entry, early vertical forearm, rotation, kick, breathing
- **Backstroke** — ear position, hip height, pinky entry, rotation
- **Breaststroke** — pull-breathe-kick-stretch timing, kick width, foot position
- **Butterfly** — chest press, hip undulation, two-kick cycle, breath height

Feedback is prioritized by speed impact: body position → catch mechanics → timing → breathing → kick.

### AI Chat Coach
Ask any swimming-related question and get cue-based, coach-style answers. The AI follows a prioritization framework and uses cause-effect corrections rather than vague advice. Non-swimming questions are declined.

### Roster Manager
Build a team roster with events, times, age group, gender, course, and LSC region.

- All 59 USA Swimming LSCs available in the region dropdown
- Multiple events per swimmer are grouped into a single row
- Entering a faster time for an existing event updates it; slower times are ignored
- Roster resets on every page load

### Time Standards
Each entered time is automatically rated against the **2024–2028 USA Swimming Motivational Standards** (B through AAAA) for the swimmer's age group, gender, and course (SCY / LCM / SCM).

### Team Assistant
A second AI chat panel for roster-level questions and team-wide analysis.

---

## Getting Started

1. Open `swimAnalysis.html` in any modern browser (Chrome, Safari, Firefox, Edge).
2. Paste your API key in the top-right field:
   - OpenAI key (`sk-...`) → uses GPT-4o
   - Anthropic key (`sk-ant-...`) → uses Claude Sonnet
3. Start uploading, chatting, or building your roster.

> If you open the project folder in a browser, `index.html` will redirect to the app automatically.

---

## Files

| File | Purpose |
|------|---------|
| `swimAnalysis.html` | Main app — all HTML, CSS, and JS in one file |
| `index.html` | Redirect to `swimAnalysis.html` |
| `swim_knowledge.md` | Coaching doctrine used as AI context |
| `USA_Swimming_2028_Motivational_Standards.csv` | Official time standards source |
| `body_detection.py` | Standalone MediaPipe pose detection (Streamlit) |
| `pose_landmarker_heavy.task` | MediaPipe model for `body_detection.py` |

---

## Coaching Doctrine (`swim_knowledge.md`)

The AI's coaching behavior is driven by `swim_knowledge.md`, which defines:

- Stroke checkpoints and ideal body positions for all four strokes
- Common faults, their causes, coaching cues, and drill prescriptions
- Video analysis rules (e.g., no catch diagnosis without underwater view)
- Language style: cue-based, prioritized, no medical diagnoses or vague advice
- Drill rules: 1–3 drills max, tied to a specific fault

---

## Privacy

- API keys are stored only in your browser's `localStorage` — never logged or shared
- No data leaves your machine except direct API calls to OpenAI or Anthropic
- The roster is not saved between sessions
