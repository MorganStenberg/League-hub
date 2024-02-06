const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");



for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let matchId = e.target.getAttribute("data-match_id");
      deleteConfirm.href = `delete_match/${matchId}`;
      deleteModal.show();
    });
  }

