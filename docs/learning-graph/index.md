---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **82 个概念、95 条先修关系**，概念按章排列，颜色表示 6 个类别（基本概念、核心技术、大模型与语言、视听与生成、智能体与应用、安全与伦理）。概念的定义都来自[附录 C 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 AI 导论（16 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [人工智能](../appendix/glossary.md#g-人工智能) | 基本概念 | — |
    | [图灵测试](../appendix/glossary.md#g-图灵测试) | 基本概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [中文房间](../appendix/glossary.md#g-中文房间) | 基本概念 | [图灵测试](../appendix/glossary.md#g-图灵测试) |
    | [符号主义](../appendix/glossary.md#g-符号主义) | 基本概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [专家系统](../appendix/glossary.md#g-专家系统) | 基本概念 | [符号主义](../appendix/glossary.md#g-符号主义) |
    | [联结主义](../appendix/glossary.md#g-联结主义) | 基本概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [行为主义](../appendix/glossary.md#g-行为主义) | 基本概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [感知机](../appendix/glossary.md#g-感知机) | 基本概念 | [联结主义](../appendix/glossary.md#g-联结主义) |
    | [机器学习](../appendix/glossary.md#g-机器学习) | 基本概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [深度学习](../appendix/glossary.md#g-深度学习) | 基本概念 | [机器学习](../appendix/glossary.md#g-机器学习)、[神经网络](../appendix/glossary.md#g-神经网络) |
    | [弱人工智能](../appendix/glossary.md#g-弱人工智能) | 基本概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [通用人工智能](../appendix/glossary.md#g-通用人工智能) | 基本概念 | [弱人工智能](../appendix/glossary.md#g-弱人工智能) |
    | [生成式人工智能](../appendix/glossary.md#g-生成式人工智能) | 基本概念 | [深度学习](../appendix/glossary.md#g-深度学习) |
    | [缩放法则](../appendix/glossary.md#g-缩放法则) | 核心技术 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [涌现](../appendix/glossary.md#g-涌现) | 核心技术 | [缩放法则](../appendix/glossary.md#g-缩放法则) |
    | [幻觉](../appendix/glossary.md#g-幻觉) | 大模型与语言 | [大语言模型](../appendix/glossary.md#g-大语言模型) |

??? note "第 2 章 机器学习的底层逻辑（12 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [神经网络](../appendix/glossary.md#g-神经网络) | 核心技术 | [联结主义](../appendix/glossary.md#g-联结主义) |
    | [激活函数](../appendix/glossary.md#g-激活函数) | 核心技术 | [神经网络](../appendix/glossary.md#g-神经网络) |
    | [损失函数](../appendix/glossary.md#g-损失函数) | 核心技术 | [神经网络](../appendix/glossary.md#g-神经网络) |
    | [梯度下降](../appendix/glossary.md#g-梯度下降) | 核心技术 | [损失函数](../appendix/glossary.md#g-损失函数) |
    | [反向传播](../appendix/glossary.md#g-反向传播) | 核心技术 | [梯度下降](../appendix/glossary.md#g-梯度下降) |
    | [过拟合](../appendix/glossary.md#g-过拟合) | 核心技术 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [卷积神经网络](../appendix/glossary.md#g-卷积神经网络) | 核心技术 | [神经网络](../appendix/glossary.md#g-神经网络) |
    | [思维链](../appendix/glossary.md#g-思维链) | 大模型与语言 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [推理模型](../appendix/glossary.md#g-推理模型) | 大模型与语言 | [思维链](../appendix/glossary.md#g-思维链)、[强化学习](../appendix/glossary.md#g-强化学习) |
    | [强化学习](../appendix/glossary.md#g-强化学习) | 核心技术 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [注意力机制](../appendix/glossary.md#g-注意力机制) | 核心技术 | [神经网络](../appendix/glossary.md#g-神经网络) |
    | [Transformer](../appendix/glossary.md#g-Transformer) | 核心技术 | [注意力机制](../appendix/glossary.md#g-注意力机制) |

??? note "第 3 章 语言智能（11 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [大语言模型](../appendix/glossary.md#g-大语言模型) | 大模型与语言 | [Transformer](../appendix/glossary.md#g-Transformer)、[预训练](../appendix/glossary.md#g-预训练) |
    | [词元](../appendix/glossary.md#g-词元) | 大模型与语言 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [词向量](../appendix/glossary.md#g-词向量) | 大模型与语言 | [神经网络](../appendix/glossary.md#g-神经网络) |
    | [预训练](../appendix/glossary.md#g-预训练) | 大模型与语言 | [Transformer](../appendix/glossary.md#g-Transformer) |
    | [微调](../appendix/glossary.md#g-微调) | 大模型与语言 | [预训练](../appendix/glossary.md#g-预训练) |
    | [人类反馈强化学习](../appendix/glossary.md#g-人类反馈强化学习) | 大模型与语言 | [微调](../appendix/glossary.md#g-微调)、[强化学习](../appendix/glossary.md#g-强化学习) |
    | [温度](../appendix/glossary.md#g-温度) | 大模型与语言 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [上下文窗口](../appendix/glossary.md#g-上下文窗口) | 大模型与语言 | [词元](../appendix/glossary.md#g-词元) |
    | [混合专家模型](../appendix/glossary.md#g-混合专家模型) | 大模型与语言 | [Transformer](../appendix/glossary.md#g-Transformer) |
    | [提示词工程](../appendix/glossary.md#g-提示词工程) | 大模型与语言 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [检索增强生成](../appendix/glossary.md#g-检索增强生成) | 大模型与语言 | [大语言模型](../appendix/glossary.md#g-大语言模型)、[词向量](../appendix/glossary.md#g-词向量) |

??? note "第 4 章 视听觉醒（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [计算机视觉](../appendix/glossary.md#g-计算机视觉) | 视听与生成 | [深度学习](../appendix/glossary.md#g-深度学习) |
    | [视觉变换器](../appendix/glossary.md#g-视觉变换器) | 视听与生成 | [Transformer](../appendix/glossary.md#g-Transformer)、[计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [生成对抗网络](../appendix/glossary.md#g-生成对抗网络) | 视听与生成 | [神经网络](../appendix/glossary.md#g-神经网络) |
    | [扩散模型](../appendix/glossary.md#g-扩散模型) | 视听与生成 | [神经网络](../appendix/glossary.md#g-神经网络)、[生成式人工智能](../appendix/glossary.md#g-生成式人工智能) |
    | [语谱图](../appendix/glossary.md#g-语谱图) | 视听与生成 | [计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [语音识别](../appendix/glossary.md#g-语音识别) | 视听与生成 | [语谱图](../appendix/glossary.md#g-语谱图) |
    | [语音合成](../appendix/glossary.md#g-语音合成) | 视听与生成 | [语谱图](../appendix/glossary.md#g-语谱图) |
    | [多模态](../appendix/glossary.md#g-多模态) | 视听与生成 | [大语言模型](../appendix/glossary.md#g-大语言模型)、[计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [深度伪造](../appendix/glossary.md#g-深度伪造) | 安全与伦理 | [生成对抗网络](../appendix/glossary.md#g-生成对抗网络)、[扩散模型](../appendix/glossary.md#g-扩散模型) |
    | [AI 生成内容标识](../appendix/glossary.md#g-AI-生成内容标识) | 安全与伦理 | [深度伪造](../appendix/glossary.md#g-深度伪造) |

??? note "第 5 章 智能体（7 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [智能体](../appendix/glossary.md#g-智能体) | 智能体与应用 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [推理—行动循环](../appendix/glossary.md#g-推理—行动循环) | 智能体与应用 | [智能体](../appendix/glossary.md#g-智能体)、[思维链](../appendix/glossary.md#g-思维链) |
    | [函数调用](../appendix/glossary.md#g-函数调用) | 智能体与应用 | [智能体](../appendix/glossary.md#g-智能体) |
    | [模型上下文协议](../appendix/glossary.md#g-模型上下文协议) | 智能体与应用 | [函数调用](../appendix/glossary.md#g-函数调用) |
    | [智能体技能](../appendix/glossary.md#g-智能体技能) | 智能体与应用 | [智能体](../appendix/glossary.md#g-智能体) |
    | [多智能体系统](../appendix/glossary.md#g-多智能体系统) | 智能体与应用 | [智能体](../appendix/glossary.md#g-智能体) |
    | [具身智能](../appendix/glossary.md#g-具身智能) | 智能体与应用 | [智能体](../appendix/glossary.md#g-智能体)、[行为主义](../appendix/glossary.md#g-行为主义) |

??? note "第 6 章 AI+X（5 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [AI+X](../appendix/glossary.md#g-AI+X) | 智能体与应用 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [三层融合模型](../appendix/glossary.md#g-三层融合模型) | 智能体与应用 | [AI+X](../appendix/glossary.md#g-AI+X) |
    | [AI for Science](../appendix/glossary.md#g-AI-for-Science) | 智能体与应用 | [AI+X](../appendix/glossary.md#g-AI+X)、[深度学习](../appendix/glossary.md#g-深度学习) |
    | [数字孪生](../appendix/glossary.md#g-数字孪生) | 智能体与应用 | [AI+X](../appendix/glossary.md#g-AI+X) |
    | [知识图谱](../appendix/glossary.md#g-知识图谱) | 智能体与应用 | [符号主义](../appendix/glossary.md#g-符号主义) |

??? note "第 7 章 AI 安全（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [提示词注入](../appendix/glossary.md#g-提示词注入) | 安全与伦理 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [越狱](../appendix/glossary.md#g-越狱) | 安全与伦理 | [提示词注入](../appendix/glossary.md#g-提示词注入) |
    | [对抗样本](../appendix/glossary.md#g-对抗样本) | 安全与伦理 | [神经网络](../appendix/glossary.md#g-神经网络) |
    | [数据投毒](../appendix/glossary.md#g-数据投毒) | 安全与伦理 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [差分隐私](../appendix/glossary.md#g-差分隐私) | 安全与伦理 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [联邦学习](../appendix/glossary.md#g-联邦学习) | 安全与伦理 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [对齐](../appendix/glossary.md#g-对齐) | 安全与伦理 | [人类反馈强化学习](../appendix/glossary.md#g-人类反馈强化学习) |
    | [护栏](../appendix/glossary.md#g-护栏) | 安全与伦理 | [对齐](../appendix/glossary.md#g-对齐)、[提示词注入](../appendix/glossary.md#g-提示词注入) |
    | [红队测试](../appendix/glossary.md#g-红队测试) | 安全与伦理 | [提示词注入](../appendix/glossary.md#g-提示词注入)、[对抗样本](../appendix/glossary.md#g-对抗样本) |
    | [内容凭证](../appendix/glossary.md#g-内容凭证) | 安全与伦理 | [AI 生成内容标识](../appendix/glossary.md#g-AI-生成内容标识) |

??? note "第 8 章 AI 伦理（11 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [人工智能伦理](../appendix/glossary.md#g-人工智能伦理) | 安全与伦理 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [独创性智力投入](../appendix/glossary.md#g-独创性智力投入) | 安全与伦理 | [生成式人工智能](../appendix/glossary.md#g-生成式人工智能) |
    | [思想与表达二分法](../appendix/glossary.md#g-思想与表达二分法) | 安全与伦理 | [独创性智力投入](../appendix/glossary.md#g-独创性智力投入) |
    | [合理使用](../appendix/glossary.md#g-合理使用) | 安全与伦理 | [思想与表达二分法](../appendix/glossary.md#g-思想与表达二分法) |
    | [算法偏见](../appendix/glossary.md#g-算法偏见) | 安全与伦理 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [代理变量](../appendix/glossary.md#g-代理变量) | 安全与伦理 | [算法偏见](../appendix/glossary.md#g-算法偏见) |
    | [大数据杀熟](../appendix/glossary.md#g-大数据杀熟) | 安全与伦理 | [算法偏见](../appendix/glossary.md#g-算法偏见) |
    | [算法公平性](../appendix/glossary.md#g-算法公平性) | 安全与伦理 | [算法偏见](../appendix/glossary.md#g-算法偏见) |
    | [恐怖谷效应](../appendix/glossary.md#g-恐怖谷效应) | 安全与伦理 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [半人马模式](../appendix/glossary.md#g-半人马模式) | 安全与伦理 | [人工智能伦理](../appendix/glossary.md#g-人工智能伦理) |
    | [信息茧房](../appendix/glossary.md#g-信息茧房) | 安全与伦理 | [算法偏见](../appendix/glossary.md#g-算法偏见) |

<!-- graph:end -->
