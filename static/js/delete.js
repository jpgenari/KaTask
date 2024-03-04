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
        let taskId = e.target.getAttribute("data-task-id"); // Use data attribute to store task ID
        deleteConfirm.href = `/delete-task/${taskId}/`; // Update with the correct URL for deleting a task
        deleteModal.show();
    });
}
