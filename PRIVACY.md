# Privacy Policy
This plugin runs on a drawing interface and lets you use a large language model (LLM) to generate mind maps and Mermaid diagrams, then insert and edit them on the canvas. The Tool is designed with a “minimal data processing” principle: it does not collect or store your personal information or canvas content. This document explains how data is handled, how the Tool interacts with LLMs, and what third‑party services may be involved.

## Scope

This policy applies to the Tool when used within the Dify ecosystem, including its endpoints (e.g., LLM generation and static page serving). If you configure external model providers in Dify (e.g., OpenAI, Azure OpenAI, Alibaba, Zhipu, etc.), you should also review the privacy policies and terms of both Dify and those providers.

## Data We Process

- No personal identifiers: The Tool does not collect, store, or process your name, email, account details, or other personal identifiers.
- No canvas or file contents: The mind maps, Mermaid text, or other content you create/edit on the canvas are not collected or persistently stored by the Tool.
- No behavior tracking: The Tool does not include analytics, advertising code, or behavior tracking; it does not profile users or log usage for analytics purposes.

## LLM Interaction and Data Transfer

- Generation purpose only: When you ask the LLM to generate mind maps or Mermaid diagrams, your prompt is sent as model input solely to produce the requested output, which is then inserted into your local canvas. Beyond what is strictly necessary to provide this feature, the Tool does not use your data for any other purpose.
- Routed by Dify: Model calls are made by the Dify runtime to the model provider you configured. The Tool does not create direct connections to external model services, nor does it independently transmit data to third parties.
- Possible third parties: Depending on your configuration, your prompts and related context may be sent to the chosen model provider (e.g., OpenAI, Azure, Alibaba, Zhipu, etc.) for processing. You should read and agree to the privacy policies and terms of both Dify and the provider before enabling such calls.

## Storage and Retention

- No persistent storage: The Tool does not persist your inputs, generated outputs, or canvas data on the plugin side.
- No long‑term logs: The Tool does not keep content‑identifiable access or debug logs on the plugin side. If Dify or a model provider retains request records for operations or compliance, that retention is governed by their respective policies.

## Security

- Transport security: Network security for calls to model providers (e.g., encryption, key management) is handled by Dify and/or the configured providers. The Tool does not add external network endpoints beyond model invocation.
- Least privilege: The Tool enables only the model capabilities required for generation and does not request unrelated permissions.

## Cookies and Tracking

The Tool does not use cookies, embed analytics/advertising pixels, or perform cross‑site/app tracking.

## Your Controls and Choices

- Model configuration is under your control: In Dify, you can choose or change model providers/versions, or use local/self‑hosted models to avoid data egress.
- You manage your assets: Your files and artifacts remain under your control in your local or self‑managed environment. The Tool does not automatically back up or upload your content.

## Third‑Party Services

If you opt to use third‑party model providers, your prompts and related context may be processed, cached, or retained by those services for compliance and safety. Review the providers’ privacy policies and data‑handling terms, and consider enabling Dify’s compliance/redaction options as needed.

## Children’s Privacy

The Tool is intended for users with full legal capacity and is not directed to children. It does not knowingly collect information from minors.

## Changes

If we make material changes to this policy, we will update this file in the repository and note the change in the release notes. The updated policy becomes effective upon publication.

## Contact

For questions about this policy or our privacy practices, please open an issue on GitHub: https://github.com/hjlarry/dify-plugin-draw
