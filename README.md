## Document Representation

Each Cranfield document will be represented using four fields:

- `document_id` — unique identifier for the document
- `title` — title of the scientific document
- `author` — author of the document
- `text` — main searchable text of the document

## Tokenizer Design

The tokenizer will use the following interface:

`tokenize(text) -> list[str]`

The tokenizer will process text in the following order:

1. Convert all text to lowercase.
2. Remove punctuation.
3. Split the text into individual words/tokens.
4. Remove stop words.
5. Return the resulting list of tokens.

For example:

`"The Aircraft flies quickly."`

will become:

`["aircraft", "flies", "quickly"]`