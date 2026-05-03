---
id: b7ff18706c
question: Why does Kestra support conditional branching within a single workflow instead
  of separate flows?
sort_order: 15
---

Kestra supports conditional branching within a single workflow to reuse shared orchestration logic while allowing dataset-specific behavior. This approach reduces duplication, keeps related steps together, and makes execution paths explicit within a single workflow definition.

When to use a single-workflow branch:
- Reuse common steps (e.g., data validation, enrichment) across datasets.
- Implement dataset-specific paths (e.g., Yellow vs Green taxi) within the same flow.

How to implement:
- Use a branching mechanism in Kestra (e.g., a condition or switch node) to evaluate a runtime variable (such as the dataset type) and route to the appropriate sub-path.
- Place shared steps before the branch; place dataset-specific steps inside each branch.
- Decide how branches converge: continue with a common tail after the branch or treat branches as separate end states.

Best practices:
- Keep branches modular and minimal; extract shared logic into subflows where possible.
- Centralize error handling and logging to ensure consistency across branches.
- Test each branch with representative inputs and monitor branch-specific failures separately.

Example (illustrative pseudo YAML):
```
- id: route_by_dataset
  type: branch
  when:
    - condition: ${workflow.variables.dataset_type == 'yellow'}
      then:
        - - id: yellow_tasks
            tasks: [ yellow_validate, yellow_transform ]
    - else:
        - - id: green_tasks
            tasks: [ green_validate, green_transform ]
- id: end
  type: terminate
```

Note: Adapt the exact branch/task names to your Kestra workflow definitions. The key idea is to place shared logic before the branch, branch on dataset/type, and then execute dataset-specific steps within each branch.