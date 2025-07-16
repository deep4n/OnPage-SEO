def create_title_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan 1 judul SEO yang panjang, deskriptif, dan relevan dengan konten halaman.

    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.

    Returns:
        str: Prompt yang disiapkan untuk menghasilkan 1 judul SEO.
    """
    prompt = (
        f"You are an SEO expert tasked with crafting a highly optimized title tag for web content. "
        f"Your goal is to generate 1 unique, detailed, and SEO-friendly title tag that includes the keyword, "
        f"while providing a comprehensive description of the page's content. The title should be descriptive, informative, "
        f"and engage the audience while clearly indicating the page's value.\n\n"
        f"Title tags are essential for conveying the main topic of a page to search engines and users. "
        f"They should clearly describe the content of the page and encourage clicks from users. "
        f"The title tag will appear as the main link in Google search results, so it must attract attention and provide a clear idea of the page’s focus.\n\n"
        f"Using the following content:\n"
        f"-----------------------------\n"
        f"{content}\n"
        f"-----------------------------\n"
        f"Generate 1 unique, detailed, and SEO-optimized title tag that includes the keyword '{keyword}' and meets the following requirements:\n\n"
        f"1. **Uniqueness**: Ensure the title tag is unique for this page.\n"
        f"2. **Keyword Usage**: Include the main keyword in the title tag, ensuring it is naturally integrated into the title.\n"
        f"3. **Length Limitation**: The title tag should be between 80-100 characters, detailed yet concise for SEO.\n"
        f"4. **Conciseness and Clarity**: Clearly describe the content, using separators like colons to break up logical sections.\n"
        f"5. **Avoid Keyword Stuffing**: Do not repeat the keyword excessively; keep it natural and informative.\n"
        f"6. **Relevance and Descriptiveness**: Capture the essence of the content, explain key benefits or outcomes.\n"
        f"7. **Language**: The title must be in English for proper indexing.\n\n"
        f"**Output Format:**\n"
        f"- Provide exactly 1 SEO title tag.\n"
        f"- Use a separator like a colon to organize key elements of the title.\n"
        f"- Present as: Title Tag\n"
        f"- Do not include any extra commentary or explanation."
    )
    return prompt

def create_meta_description_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan 1 meta description yang efektif dan sesuai dengan SEO terbaik.

    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.

    Returns:
        str: Prompt yang disiapkan untuk menghasilkan 1 meta description.
    """
    prompt = (
        f"You are an SEO expert tasked with creating a highly optimized meta description. "
        f"Your goal is to generate 1 unique and compelling meta description that accurately reflects the content of the page "
        f"and adheres to SEO best practices, providing a clear and engaging summary.\n\n"
        f"Meta descriptions appear under the title in search results and should entice users to click by clearly explaining what they can expect. "
        f"Google may choose to display other text if the meta description is not informative enough.\n\n"
        f"Using the following content:\n"
        f"-----------------------------\n"
        f"{content}\n"
        f"-----------------------------\n"
        f"Generate 1 unique and detailed meta description that includes the keyword '{keyword}' and meets the following criteria:\n\n"
        f"1. **Use the Main Keyword**: The main keyword should be naturally included.\n"
        f"2. **Uniqueness**: Must be unique for this page.\n"
        f"3. **Avoid Generic Descriptions**: Be specific and reflect the actual content.\n"
        f"4. **Length Limitation**: 140-160 characters so it displays fully in search results.\n"
        f"5. **Engaging and Informative**: Grab attention and encourage clicks with enough detail.\n"
        f"6. **Consistency with Content**: Clearly represent what users can expect.\n"
        f"7. **Relevance to Search Intent**: Match user search intent and be useful for their needs.\n"
        f"8. **Language**: The description must be in English.\n\n"
        f"**Output Format:**\n"
        f"- Output only the meta description text.\n"
        f"- Do not include any label, prefix (like 'Meta Description:'), explanation, or formatting.\n"
        f"- Just return the raw meta description in one line.\n"
    )
    return prompt

def create_url_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan 1 URL yang dioptimalkan.

    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.

    Returns:
        str: Prompt yang disiapkan untuk menghasilkan 1 URL.
    """
    prompt = (
        f"You are an SEO expert tasked with creating an optimized URL. "
        f"Your goal is to generate 1 concise, descriptive, and SEO-friendly URL that includes the main keyword and follows best practices for URL structure.\n\n"
        f"Using the following content:\n"
        f"-----------------------------\n"
        f"{content}\n"
        f"-----------------------------\n"
        f"Generate 1 optimized URL that includes the keyword '{keyword}' and meets the following criteria:\n\n"
        f"1. **Use the Main Keyword**: The URL must contain the main keyword.\n"
        f"2. **Descriptive and Clear**: The URL should clearly describe the content.\n"
        f"3. **Ideal URL Length**: Keep it short and memorable.\n"
        f"4. **Simple and Structured**: Easy to understand and well-organized.\n"
        f"5. **User-Friendly**: Avoid hard-to-understand characters.\n"
        f"6. **Avoid Unnecessary Characters**: Only include relevant text.\n\n"
        f"**Output Format:**\n"
        f"- Provide exactly 1 URL.\n"
        f"- Present as: /Optimized URL\n"
        f"- Do not include any extra commentary or explanation."
    )
    return prompt