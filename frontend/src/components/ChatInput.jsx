import { useState } from "react";
import API from "../services/api";
import materialImages from "../utils/materialImages";
function ChatInput() {

  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {

    if (!prompt.trim()) return;

    try {

      setLoading(true);
 
      const response = await API.post(
        "/chat-recommend",
        {
          text: prompt
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);
      alert("Backend connection failed");

    } finally {

      setLoading(false);

    }
  };

  return (

    <div className="card bg-base-100 shadow-xl p-6">

      <h2 className="text-2xl font-bold mb-4">
        Describe Your Requirement
      </h2>

      <textarea
        className="
      w-full
      px-4
      py-3
      rounded-xl
      bg-slate-800
      border
      border-slate-600
      text-white
      placeholder-slate-400
      focus:outline-none
      focus:border-cyan-400
      focus:ring-2
      focus:ring-cyan-500/30
      transition-all
    "
        placeholder="Example: I need lightweight material for high-speed machinery..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        className="
    mt-8
    px-10
    py-4
    bg-cyan-500
    hover:bg-cyan-400
    rounded-xl
    text-lg
    font-bold
    shadow-lg
    hover:scale-105
    transition-all
  "
        onClick={handleSubmit}
      >
        {loading ? "Analyzing..." : "Analyze Requirement"}
      </button>

      {/* RESULT SECTION */}

      {result && (

        <div className="mt-6">

          <h3 className="text-xl font-bold mb-2">
            Extracted Parameters
          </h3>

          <div className="bg-base-200 p-4 rounded-lg">

            <p>
              Hardness:
              {" "}
              {result.extracted_parameters.hardness}
            </p>

            <p>
              Density:
              {" "}
              {result.extracted_parameters.density}
            </p>

            <p>
              Temperature:
              {" "}
              {result.extracted_parameters.temperature}
            </p>

            <p>
              Load:
              {" "}
              {result.extracted_parameters.load}
            </p>

            <p>
              Speed:
              {" "}
              {result.extracted_parameters.speed}
            </p>

          </div>

          <h3 className="text-xl font-bold mt-6 mb-2">
            Predicted Properties
          </h3>

          <div className="bg-base-200 p-4 rounded-lg">

            <p>
              Wear Rate:
              {" "}
              {result.predicted_properties.WearRate}
            </p>

            <p>
              Friction Coefficient:
              {" "}
              {result.predicted_properties.FrictionCoefficient}
            </p>

          </div>

          <h3 className="text-xl font-bold mt-6 mb-2">
            Recommended Materials
          </h3>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

  {
    result.recommended_materials.map(
      (material, index) => (

        <div
          key={index}
          className="card bg-base-200 shadow-md p-4 hover:shadow-xl transition-all duration-300"
        >
          <img
  src={
    materialImages[material.Material]
  }
  alt={material.Material}
  className="
    w-full
    h-56
    object-cover
    rounded-xl
    mb-4
    shadow-lg
  "
/>

          <h4 className="text-xl font-bold mb-2">
            {material.Material}
          </h4>

          <div className="space-y-2">

            <p>
              <span className="font-semibold">
                Similarity:
              </span>
              {" "}
              {material.SimilarityScore}%
            </p>

            <p>
              <span className="font-semibold">
                Wear Rate:
              </span>
              {" "}
              {material.WearRate}
            </p>

            <p>
              <span className="font-semibold">
                Friction:
              </span>
              {" "}
              {
                material.FrictionCoefficient
              }
            </p>
            <p className="mt-3 text-sm text-gray-500 leading-relaxed">

                {material.Explanation}

             </p>


          </div>

          {/* PROGRESS BAR */}

          <progress
            className="progress progress-primary w-full mt-4"
            value={material.SimilarityScore}
            max="100"
          />

        </div>
      )
    )
  }

</div>

        </div>

      )}

    </div>
  );
}

export default ChatInput;