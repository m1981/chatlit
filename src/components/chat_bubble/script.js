export default function(component) {
    const { setTriggerValue, data, parentElement } = component;

    const contentDiv = parentElement.querySelector('#content');
    const btnEdit = parentElement.querySelector('#btn-edit');
    const btnStar = parentElement.querySelector('#btn-star');
    const btnMore = parentElement.querySelector('#btn-more');

    // 1. Render Content
    // We simply inject the text passed from Python
    if (contentDiv.innerText !== data.content) {
        contentDiv.innerText = data.content;
    }

    // 2. Handle Star State (Visual only)
    if (data.is_starred) {
        btnStar.classList.add('active');
    } else {
        btnStar.classList.remove('active');
    }

    // 3. Event Listeners -> Send Triggers to Python
    // We use 'setTriggerValue' because clicks are transient events.

    btnEdit.onclick = () => {
        setTriggerValue('edit_clicked', data.id);
    };

    btnStar.onclick = () => {
        // Toggle visual state immediately for responsiveness
        btnStar.classList.toggle('active');
        setTriggerValue('star_clicked', data.id);
    };

    btnMore.onclick = () => {
        setTriggerValue('more_clicked', data.id);
    };
}