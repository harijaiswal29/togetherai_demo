// Streaming: print tokens as they arrive.  Run:  TOGETHER_API_KEY=... node stream.mjs
import Together from "together-ai";

const together = new Together();
const model = process.env.TOGETHER_MODEL ?? "meta-llama/Llama-3.3-70B-Instruct-Turbo";

const stream = await together.chat.completions.create({
  model,
  messages: [{ role: "user", content: "Write a 4-line poem about monsoon rain in Mumbai." }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
process.stdout.write("\n");
