const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated task's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific task.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let taskId = e.target.getAttribute("data-task-id");
        let categoryId = e.target.getAttribute("data-category-id");

        if (taskId) {
            deleteConfirm.href = `/delete-task/${taskId}/`;
        } else if (categoryId) {
            deleteConfirm.href = `/delete-category/${categoryId}/`;
        }

        deleteModal.show();
    });
}