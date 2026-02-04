export default function(component) {
    const { setTriggerValue, data, parentElement } = component;
    const container = parentElement.querySelector('#nav-container');

    // Clear previous render
    container.innerHTML = '';

    // Data structure: { "Work": ["Chat A", "Chat B"], "Personal": ["Chat C"] }
    const folders = data.folders;
    const activeChat = data.active_chat;

    Object.keys(folders).forEach(folderName => {
        const chats = folders[folderName];

        // 1. Create Folder Header
        const folderDiv = document.createElement('div');
        folderDiv.className = 'folder-header';
        folderDiv.innerHTML = `<span class="folder-icon">📁</span> ${folderName}`;

        // 2. Create Folder Content Container
        const contentDiv = document.createElement('div');
        contentDiv.className = 'folder-content';

        // Toggle Logic
        let isOpen = true; // Default open
        folderDiv.onclick = () => {
            isOpen = !isOpen;
            contentDiv.style.display = isOpen ? 'flex' : 'none';
            folderDiv.querySelector('.folder-icon').innerText = isOpen ? '📁' : '📂';
        };

        // 3. Create Chat Items
        chats.forEach(chatName => {
            const chatDiv = document.createElement('div');
            chatDiv.className = `chat-item ${chatName === activeChat ? 'active' : ''}`;
            chatDiv.innerText = `💬 ${chatName}`;

            chatDiv.onclick = (e) => {
                e.stopPropagation(); // Prevent folder toggle
                setTriggerValue('chat_selected', chatName);
            };

            contentDiv.appendChild(chatDiv);
        });

        container.appendChild(folderDiv);
        container.appendChild(contentDiv);
    });
}