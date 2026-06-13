import { useState } from "react";
import InputModeSelector from "./components/InputModeSelector";
import TechnicalForm from "./components/TechnicalForm";
import ChatInput from "./components/ChatInput";
import hero from "./assets/hero.png";
function App() {
  const [mode, setMode] = useState("technical");

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">

      <div className="max-w-7xl mx-auto px-6 py-10">

        {/* HEADER */}

        <div className="text-center mb-12">
           <img
    src={hero}
    alt="AI Material Recommendation System"
    className="
      w-48
      md:w-48
      mx-auto
      mb-6
      drop-shadow-2xl
    "
  />

          <h1 className="
            text-4xl
            md:text-6xl
            font-extrabold
            tracking-tight
            mb-4
          ">
            AI Material Recommendation System
          </h1>

          <p className="
            text-slate-300
            text-base
            md:text-xl
            max-w-3xl
            mx-auto
          ">
            Intelligent AI-powered material selection
            using AutoML, Explainable AI and
            Recommendation Systems
          </p>

        </div>

        {/* MODE SELECTOR */}

        <div className="mb-10">
          <InputModeSelector
            mode={mode}
            setMode={setMode}
          />
        </div>

        {/* MAIN CONTENT */}

        <div className="max-w-5xl mx-auto">

          {mode === "technical"
            ? <TechnicalForm />
            : <ChatInput />
          }

        </div>

        {/* FOOTER */}

        <footer className="
          mt-20
          text-center
          text-slate-400
          text-sm
          border-t
          border-slate-700
          pt-6
        ">
          © 2026 AI Material Recommendation System
          <br />
          Built with React, FastAPI, AutoML and Explainable AI
        </footer>

      </div>

    </div>
  );
}

export default App;