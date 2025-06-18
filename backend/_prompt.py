def create_title_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan judul SEO yang optimal.
    
    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.
    
    Returns:
        str: Prompt yang disiapkan untuk menghasilkan judul.
    """
    prompt = f"Based on the following content: {content}, create a unique SEO title that includes the keyword '{keyword}' and follows these criteria:\n" \
             "a. **Uniqueness**: Each page should have a unique title to improve page relevance.\n" \
             "b. **Keyword Usage**: Ensure the main keyword is included in the title.\n" \
             "c. **Title Length**: Keep the title length under 68 characters.\n" \
             "d. **Conciseness and Clarity**: Make the title short and descriptive.\n" \
             "e. **Avoid Keyword Stuffing**: Do not overuse or repeat the keyword excessively.\n" \
             "f. **Relevance to Audience and Topic**: Ensure the title is relevant and appropriate.\n" \
             "g. **Language**: The title must be in English to ensure proper indexing by search engines."
    return prompt

def create_meta_description_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan meta description yang efektif.
    
    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.
    
    Returns:
        str: Prompt yang disiapkan untuk menghasilkan meta description.
    """
    prompt = f"Based on the following content: {content}, create a unique meta description that includes the keyword '{keyword}' and follows these criteria:\n" \
             "a. **Use the Main Keyword**: Ensure the main keyword is included in the meta description.\n" \
             "b. **Unique for Each Page**: Create a unique description for this page.\n" \
             "c. **Avoid Generic Descriptions**: Ensure the description clearly reflects the page’s content.\n" \
             "d. **Ideal Length**: Keep the meta description under 160 characters.\n" \
             "e. **Engaging and Informative**: The description should attract the user and provide enough information.\n" \
             "f. **Consistency with Content**: The meta description should be consistent with the content on the page."
    return prompt

def create_url_prompt(content, keyword):
    """
    Membuat prompt untuk menghasilkan URL yang dioptimalkan.
    
    Args:
        content (str): Isi konten halaman.
        keyword (str): Kata kunci utama.
    
    Returns:
        str: Prompt yang disiapkan untuk menghasilkan URL.
    """
    prompt = f"Based on the following content: {content}, create an optimized URL that includes the keyword '{keyword}' and follows these criteria:\n" \
             "a. **Use the Main Keyword**: Ensure the URL contains the main keyword.\n" \
             "b. **Descriptive and Clear**: The URL should be clear and descriptive of the content.\n" \
             "c. **Ideal URL Length**: Ensure the URL is short and memorable.\n" \
             "d. **Simple and Structured URL Organization**: The URL should be easy to understand and organized.\n" \
             "e. **Use User-Friendly Text**: Avoid using hard-to-understand characters in the URL.\n" \
             "f. **Avoid Duplicate URLs**: Ensure only one version of the URL is available.\n" \
             "g. **Avoid Unnecessary Characters**: Ensure the URL is clean and only contains relevant text."
    return prompt
