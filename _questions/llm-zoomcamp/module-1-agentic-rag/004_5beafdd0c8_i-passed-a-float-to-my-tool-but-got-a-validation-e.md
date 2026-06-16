---
id: 5beafdd0c8
question: I passed a float to my tool, but got a validation error saying it expected
  a number. Isn’t float a number?
sort_order: 4
---

Yes — in Python, `float` is a numeric type. But when working with FastMCP, tool inputs are validated against JSON Schema, which uses the term "number" to represent any numeric value (integers or floats).

The important thing is not the type you use in Python, but whether the JSON you send matches the tool's declared input schema.

Example:

```json
"inputSchema": {
  "type": "object",
  "properties": {
    "temp": {
      "type": "number"
    }
  },
  "required": ["temp"]
}
```

Make sure the values in "arguments" match the types declared in the tool’s schema — not Python types, but JSON types (string, number, boolean, etc.).