<!-- edit user modal -->
<div class="modal fade" id="modal-edit-user">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id='edit-modal_title'></h4>
        <button type="button" class="close" data-dismiss="modal" aria-label="Non">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="#" method="POST" id="form-edit-user">
          <div class="form-group row">
            <label for="inputNewUsername" class="col-sm-3 col-form-label">Username</label>
            <div class="col-sm-9">
              <input type="text" class="form-control" placeholder="Username" id="edit-username" name="username" required autofocus>
            </div>
          </div>
          <div class="form-group row">
            <label for="inputTypeUser" class="col-sm-3 col-form-label">Role</label>
            <div class="col-sm-9">
              <select class="form-control" id="edit-role" name="role">
                <option value="1">ADMIN</option>
                <option value="2">GERANT</option>
                <option value="3">VENDEUR</option>
              </select>
            </div>
          </div>
          <input type="hidden" id="edit-id_user" name="id_user">
      </div>
      <div class="modal-footer justify-content-between">
        <button type="submit" class="btn btn-primary">Valider</button>
        <button type="reset" class="btn btn-default" data-dismiss="modal">Annuler</button>
      </div>
      </form>
    </div>
    <!-- /.modal-content -->
  </div>
  <!-- /.modal-dialog -->
</div>

<!-- jQuery -->
<script src="plugins/jquery/jquery.min.js"></script>

<script>
  $('#form-edit-user').submit(function(event) {
    event.preventDefault();
    $.ajax({
      url: "models/user.model.php",
      type: "post",
      timeout: 30000,
      data: "action=update&" + $('#form-edit-user').serialize(),
      cache: false,
      success: function(response) {
        jresponse = JSON.parse(response);
        if (jresponse.type == 1) {
          notif('success', jresponse.message);
          setTimeout(function() {
            window.location.reload(false);
          }, 1000);
        } else {
          notif('error', jresponse.message);
        }
      },
      error: function() {
        notif('error', "Impossible d'effectuer la modification !");
        setTimeout(function() {
          window.location.reload(false);
        }, 1000);
      },
    });
  });

  function init_form_edit_user(id_user) {
    $('#form-edit-user')[0].reset();
    $.ajax({
      url: "models/user.model.php",
      type: "post",
      timeout: 30000,
      data: "action=get_by_id&id_user=" + id_user,
      cache: false,
      success: function(response) {
        // console.log(response);
        jresponse = JSON.parse(response);
        if (!jQuery.isEmptyObject(jresponse)) {
          $("#edit-id_user").val(jresponse.id_user);
          $("#edit-username").val(jresponse.username);
          $("#edit-modal_title")[0].innerHTML = "Modifier Utilisateur: " + jresponse.username;
          $("#edit-role").val(jresponse.role);
          $("#modal-edit-user").modal("show");
        } else {
          notif('error', 'Impossible charger la modification !');
        }
      },
      error: function() {
        notif('error', 'Impossible charger la modification !');
        setTimeout(function() {
          window.location.reload(false);
        }, 1000);
      },
    });
    return false;
  }
</script>