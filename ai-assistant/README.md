# NeuroSync AI Assistant

NeuroSync AI is a production-style multimodal AI assistant built for portfolio and resume impact. It combines real-time voice interaction, a 3D robotic avatar, emotion-aware responses, AI model routing, streaming chat, and a modern cyberpunk user interface.

## Highlights

- **Multimodal conversational AI** with real-time WebSocket streaming
- **Voice assistant** using browser speech-to-text and natural TTS
- **Animated 3D robot avatar** using React Three Fiber
- **Emotion detection** driving robotic facial expressions
- **MongoDB-backed conversation memory** and session persistence
- **Modern portfolio UI** with glassmorphism, cyberpunk visuals, and responsive layout
- **Backend architecture** with FastAPI, async I/O, AI provider abstraction, and secure authentication

## Folder structure

- `frontend/` – Next.js + TypeScript + Tailwind frontend
- `backend/` – FastAPI backend with AI provider routing and WebSocket streaming
- `.env.example` – environment variable reference
- `README.md` – project documentation and deployment notes

## Resume-worthy bullets

- Built a multimodal AI assistant with real-time voice interaction and 3D avatar animation.
- Developed WebSocket-based streaming AI architecture using FastAPI and Next.js.
- Integrated speech recognition, text-to-speech, and emotion-aware avatar expressions.
- Implemented AI provider abstraction for OpenAI and OpenRouter with MongoDB-backed session memory.

## Setup guide

1. Copy `.env.example` to `backend/.env` and configure your API credentials.
2. Install backend dependencies:
   - `cd backend && python -m pip install -r requirements.txt`
3. Install frontend dependencies:
   - `cd ../frontend && npm install`
4. Run backend:
   - `cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
5. Run frontend:
   - `cd frontend && npm run dev`

## Deployment

- Frontend: Vercel deployment with `npm run build`
- Backend: Deploy on Render or Railway using `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Use secure environment variables for API keys and token secrets

## Future improvements

- Add multi-agent comparison mode for GPT, Claude, and Gemini
- Add a GLTF model loader with custom robot assets
- Add federated user authentication and multi-user profiles
- Add server-side TTS with baked voice output
- Add persistent cloud storage for chat transcripts
