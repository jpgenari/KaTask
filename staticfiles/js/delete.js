// Task deletion constants
const taskDeleteButtons = document.getElementsByClassName("btn-task-delete");
const taskDeleteModal = new bootstrap.Modal(document.getElementById("taskDeleteModal"));
const taskDeleteConfirm = document.getElementById("taskDeleteConfirm");

// Category deletion constants
const categoryDeleteButtons = document.getElementsByClassName("btn-category-delete");
const categoryDeleteModal = new bootstrap.Modal(document.getElementById("categoryDeleteModal"));
const categoryDeleteConfirm = document.getElementById("categoryDeleteConfirm");

// // Function to handle task deletion
// function handleTaskDeletion(taskId) {
//     taskDeleteConfirm.href = `/delete-task/${taskId}/`;
//     taskDeleteModal.show();
// }

// // Function to handle category deletion
// function handleCategoryDeletion(categoryId) {
//     categoryDeleteConfirm.href = `/delete-category/${categoryId}/`;
//     categoryDeleteModal.show();
// }

// // Attach event listeners for task delete buttons
// for (let button of taskDeleteButtons) {
//     button.addEventListener("click", (e) => {
//         let taskId = e.target.getAttribute("data-task-id");
//         if (taskId) {
//             handleTaskDeletion(taskId);
//         }
//     });
// }

// // Attach event listeners for category delete buttons
// for (let button of categoryDeleteButtons) {
//     button.addEventListener("click", (e) => {
//         let categoryId = e.target.getAttribute("data-category-id");
//         if (categoryId) {
//             handleCategoryDeletion(categoryId);
//         }
//     });
// }

for (let button of taskDeleteButtons) {
    button.addEventListener("click", (e) => {
        let taskId = e.target.getElementById("data-task-id");
        taskDeleteConfirm.href = `/delete-task/${taskId}/`,
        taskDeleteModal.show();
    });
}