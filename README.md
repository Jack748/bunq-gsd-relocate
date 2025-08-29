# bunq-relocation — GSD Day Demo

One-line: An LLM assistant that generates a structured relocation guide and checklist, with ticking/updates and provenance.

## Quickstart (what I'll demo)
1. run `python main.py` — generates guide and checklist
2. Open `relocation_guide.md` and `relocation_checklist.json` and `output/relocation_checklist.md`

## Fallback
If the LLM/API is unavailable you can find some previously generated files as examples called fallbacks_* in the output folder


## Checklist Schema
Each checklist item:
{
  "task": "Research Housing Market",
  "deadline": "3 months before moving",
  "description": "...",
  "links": "...",
}

## Future Implementations
1. LLM uses embedding and RAG for factual relocating data and for specific countries
2. Pipeline to clean/sanitize scraped content
3. Adapt code to retrieve real users data 
3. Add UI with interactive part (chat with LLM + option to tick boxes)
4. Add checks for monitoring of how good factual data is
5. Add Documentation and User Guides
6. GDPR: Security and Compliance
7. Add Continuous Learning and Improvement
8. Could be host for free on a website as used for client acquisition