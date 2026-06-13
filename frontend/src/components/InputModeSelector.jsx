function InputModeSelector({ mode, setMode }) {
  return (
    <div className="flex justify-center gap-4 mb-10">

  <button
    onClick={() => setMode("technical")}
    className={`
      px-6
      py-3
      rounded-xl
      font-semibold
      transition-all
      duration-300
      shadow-lg
      ${
        mode === "technical"
          ? "bg-cyan-500 text-white scale-105"
          : "bg-slate-700 text-slate-300 hover:bg-slate-600"
      }
    `}
  >
    ⚙ Technical Parameters
  </button>

  <button
    onClick={() => setMode("chat")}
    className={`
      px-6
      py-3
      rounded-xl
      font-semibold
      transition-all
      duration-300
      shadow-lg
      ${
        mode === "chat"
          ? "bg-cyan-500 text-white scale-105"
          : "bg-slate-700 text-slate-300 hover:bg-slate-600"
      }
    `}
  >
    🤖 Describe Requirement
  </button>

</div>
  );
}

export default InputModeSelector;