from omnisearch import AgentOrchestrator, KnowledgeBase

# 初始化企业知识库（集成向量库）
kb = KnowledgeBase(vector_db="milvus", embedding_model="text-embedding-004")

# 构建多 Agent 编排引擎
engine = AgentOrchestrator(
    model_config={
        "primary": "gemini-1.5-pro",
        "secondary": "gemini-1.5-flash"
    },
    reflection_enabled=True,
    max_context_window=128000
)

# 执行长链条推理任务
result = engine.execute(
    prompt="分析过去三年的供应链波动，并结合最新的合规标准生成风险预警报告",
    data_source=kb.query("supply_chain_2023_2026_reports")
)

print(f"Token Usage for this task: {result.usage.total_tokens}")