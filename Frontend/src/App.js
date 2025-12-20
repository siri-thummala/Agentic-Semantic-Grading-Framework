import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [modelAnswer, setModelAnswer] = useState("");
  const [studentAnswer, setStudentAnswer] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/evaluate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
          model_answer: modelAnswer,
          student_answer: studentAnswer,
        }),
      });

      if (!response.ok) {
        throw new Error("Backend error");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Unable to evaluate answer. Check backend connection.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>Semantic Answer Evaluation System</h2>

      <h4>Question</h4>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{ width: "500px", padding: "6px" }}
      />

      <h4>Reference / Model Answer</h4>
      <textarea
        rows="4"
        cols="70"
        value={modelAnswer}
        onChange={(e) => setModelAnswer(e.target.value)}
        placeholder="Enter reference / textbook answer"
      />


      <h4>Student Answer</h4>
      <textarea
        rows="6"
        cols="70"
        value={studentAnswer}
        onChange={(e) => setStudentAnswer(e.target.value)}
        style={{ padding: "6px" }}
      />

      <br /><br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Evaluating..." : "Evaluate Answer"}
      </button>

      {error && (
        <p style={{ color: "red" }}>{error}</p>
      )}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Evaluation Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;

