// Minimal chat request from Node.js.  Run:  TOGETHER_API_KEY=... node chat.mjs
import Together from "together-ai";

const together = new Together(); // reads TOGETHER_API_KEY
const model = process.env.TOGETHER_MODEL ?? "meta-llama/Llama-3.3-70B-Instruct-Turbo";

const response = await together.chat.completions.create({
  model,
  messages: [
    { role: "system", content: "You are a friendly travel assistant. Answer in 5 bullet points." },
    { role: "user", content: "I'm going to Goa in December for 4 days. What should I pack?" },
  ],
  max_tokens: 300,
});

console.log(response.choices[0].message.content);
