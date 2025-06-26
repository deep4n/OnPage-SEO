def create_title_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan 5 judul SEO yang panjang, deskriptif, dan relevan dengan konten halaman.

    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.

    Returns:
        str: Prompt yang disiapkan untuk menghasilkan 5 judul SEO.
    """
    prompt = (
        f"You are an SEO expert tasked with crafting highly optimized title tags for web content. "
        f"Your goal is to generate 5 unique, detailed, and SEO-friendly title tags that include the keyword, "
        f"while providing a comprehensive description of the page's content. The title should be descriptive, informative, "
        f"and engage the audience while clearly indicating the page's value.\n\n"
        f"Title tags are essential for conveying the main topic of a page to search engines and users. "
        f"They should clearly describe the content of the page, while providing enough information to encourage clicks from users. "
        f"The title tag will appear as the main link in Google search results, so it must attract attention and provide a clear idea of the page’s focus.\n\n"
        f"Using the following content:\n"
        f"-----------------------------\n"
        f"{content}\n"
        f"-----------------------------\n"
        f"Generate 5 unique, detailed, and SEO-optimized title tags that include the keyword '{keyword}' and meet the following requirements:\n\n"
        f"1. **Uniqueness**: Ensure each title tag is unique for this page to avoid duplication across pages.\n"
        f"2. **Keyword Usage**: Include the main keyword in the title tag, ensuring it is naturally integrated into the title.\n"
        f"3. **Length Limitation**: The title tag should be between 80-100 characters, ensuring the title is detailed yet concise enough for SEO. "
        f"This length will allow for the inclusion of 9-12 key elements of the content without being too long or too short.\n"
        f"4. **Conciseness and Clarity**: The title should clearly describe the content of the page, using separators like colons to break up the title into logical sections. "
        f"Make sure the title provides a comprehensive explanation of the main idea, while being easily readable.\n"
        f"5. **Avoid Keyword Stuffing**: Do not repeat the keyword excessively. The title should sound natural and remain informative.\n"
        f"6. **Relevance and Descriptiveness**: The title should capture the essence of the content, explaining key benefits, services, or outcomes that the page provides. "
        f"Ensure the title gives the audience a clear understanding of the value the page offers.\n"
        f"7. **Language**: The title must be in English to ensure proper indexing by search engines.\n\n"
        f"**Output Format:**\n"
        f"- Provide exactly 5 SEO title tags.\n"
        f"- Use separators like colons to organize key elements of the title.\n"
        f"- Ensure the titles are detailed, informative, and reflective of the page’s content.\n"
        f"- The titles should consist of 9-12 key points that summarize the core aspects of the content.\n"
        f"- Present them as a numbered list (1. Title 1, 2. Title 2, ...).\n"
        f"- Do not include any extra commentary or explanation."
    )
    return prompt


def create_meta_description_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan 5 meta description yang efektif dan sesuai dengan SEO terbaik.

    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.

    Returns:
        str: Prompt yang disiapkan untuk menghasilkan 5 meta description.
    """
    prompt = (
        f"You are an SEO expert tasked with creating highly optimized meta descriptions. "
        f"Your goal is to generate 5 unique and compelling meta descriptions that accurately reflect the content of the page "
        f"and adhere to SEO best practices, while providing a clear and engaging summary of the page.\n\n"
        f"Meta description tags are important for conveying the main idea of the page to search engines and users. "
        f"They appear under the title in search results and should entice users to click on the link by clearly explaining what they can expect. "
        f"However, Google may also choose to display text from other sections of the page if the meta description is not informative enough.\n\n"
        f"Using the following content:\n"
        f"-----------------------------\n"
        f"{content}\n"
        f"-----------------------------\n"
        f"Generate 5 unique and detailed meta descriptions that include the keyword '{keyword}' and meet the following criteria:\n\n"
        f"1. **Use the Main Keyword**: Ensure the main keyword is included in the meta description in a natural way.\n"
        f"2. **Uniqueness**: The meta description must be unique for each page. Avoid using the same description across multiple pages.\n"
        f"3. **Avoid Generic Descriptions**: The description should be specific and reflect the actual content of the page, without being vague.\n"
        f"4. **Length Limitation**: Each meta description should be **between 140-160 characters** to ensure it displays fully in search results. "
        f"Descriptions that are too short may not provide enough information, while those too long may be cut off.\n"
        f"5. **Engaging and Informative**: The meta description should grab the user’s attention and encourage them to click. It should give enough detail about the page's content.\n"
        f"6. **Consistency with Content**: The meta description should be aligned with the page’s content and clearly represent what users can expect when they visit the page.\n"
        f"7. **Relevance to Search Intent**: Ensure the meta description matches the user’s search intent, making it relevant to their query and useful for their needs.\n"
        f"8. **Language**: The title must be in English to ensure proper indexing by search engines.\n\n"
        f"**Output Format:**\n"
        f"- Provide exactly 5 meta descriptions.\n"
        f"- Make sure each description is distinct, clear, and well-structured.\n"
        f"- Present them as a numbered list (1. Meta Description 1, 2. Meta Description 2, ...).\n"
        f"- Avoid including any extra commentary or explanation.\n"
    )
    return prompt



def create_url_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan 5 URL yang dioptimalkan.

    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.

    Returns:
        str: Prompt yang disiapkan untuk menghasilkan 5 URL.
    """
    prompt = (
        f"You are an SEO expert tasked with creating optimized URLs. "
        f"Your goal is to generate five concise, descriptive, and SEO-friendly URLs that include the main keyword and follow best practices for URL structure.\n\n"
        f"Using the following content:\n"
        f"-----------------------------\n"
        f"{content}\n"
        f"-----------------------------\n"
        f"Generate 5 optimized URLs that include the keyword '{keyword}' and meet the following criteria:\n\n"
        f"1. **Use the Main Keyword**: Ensure the URL contains the main keyword.\n"
        f"2. **Descriptive and Clear**: The URL should be clear and descriptive of the content.\n"
        f"3. **Ideal URL Length**: Keep the URL short and memorable.\n"
        f"4. **Simple and Structured URL Organization**: The URL should be easy to understand and organized.\n"
        f"5. **Use User-Friendly Text**: Avoid using hard-to-understand characters in the URL.\n"
        f"6. **Avoid Duplicate URLs**: Ensure there is only one version of the URL available.\n"
        f"7. **Avoid Unnecessary Characters**: The URL should be clean, containing only relevant text.\n\n"
        f"**Output Format:**\n"
        f"- Provide exactly 5 URLs.\n"
        f"- Present them as a numbered list (1. URL 1, 2. URL 2, ...).\n"
        f"- Do not include any extra commentary or explanation."
    )
    return prompt
