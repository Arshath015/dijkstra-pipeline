# Dijkstra Pipeline Analysis

**Objective**: Verify that the staged architecture does not introduce measurable overhead compared to a monolithic implementation.

*Method*: We generated a random sparse graph with 10,000 nodes and ~30,000 edges. The monolithic version (single function) and the staged pipeline were each executed 5 times; wall‑clock times were recorded using `time.perf_counter`.

*Result*: The pipeline added ~0.003 s overhead on average, well within acceptable limits for internal utilities. The modularity gain—clear separation of loading, computation, and formatting—outweighs the negligible performance cost.
