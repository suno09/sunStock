<?php
include_once('models/database.model.php');

$nshow = 10;
if (isset($_GET['npage']) && $_GET['npage'] > -1)
    $npage = $_GET['npage'];
else
    $npage = 0;

$len_users = Database::execute_query_with_prepared_statement_and_first_row(
    "select count(*) as len_users from users where active=1 and id_user > 1;")['len_users'];

$result = Database::execute_query_with_prepared_statement(
    "select id_user, username, role, 
    case role 
    when 1 then 'ADMIN'
    when 2 then 'GERANT'
    when 3 then 'VENDEUR' end as rolen
    from users where active=1 and id_user > 1 order by username limit ?, ?;",
    array($npage * $nshow, $nshow)
);
?>
<section class="content">
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Utilisateurs</h3>
            <div class="card-tools">
                <div class="input-group input-group-sm" style="width: 300px;">
                    <input type="text" name="table_search" class="form-control float-right" placeholder="Rechercher" onkeyup="filter_table_users();">
                    <div class="input-group-append">
                        <button type="" class="btn btn-default" disabled><i class="fas fa-search"></i></button>
                    </div>
                </div>
            </div>
        </div>
        <!-- /.card-header -->
        <div class="card-body table-responsive p-0">
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Utilisateur</th>
                        <th>Role</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = $npage * $nshow + 1;
                    while ($row = $result->fetch_assoc()) { ?>
                        <tr>
                            <td>
                                <?php echo $i; ?>
                            </td>
                            <td>
                                <?php echo $row['username']; ?>
                            </td>
                            <td>
                                <?php echo $row['rolen']; ?>
                            </td>
                            <td class="project-actions text-left">
                                <a class="btn btn-info btn-sm" title="Modifier" href="#" onclick="init_form_edit_user(<?php echo $row['id_user']; ?>);">
                                    <i class="fas fa-pencil-alt">
                                    </i>
                                </a>
                                <a class="btn btn-success btn-sm" title="Changer mot de passe" href="#" onclick="init_form_change_password(<?php echo $row['id_user']; ?>);">
                                    <i class="fas fa-key">
                                    </i>
                                </a>
                                <a class="btn btn-danger btn-sm" title="Supprimer" href="#" onclick="init_form_delete_user(<?php echo $row['id_user']; ?>);">
                                    <i class="fas fa-trash">
                                    </i>
                                </a>
                            </td>
                        </tr>
                    <?php $i++;
                    } ?>
                </tbody>
            </table>
        </div>
        <!-- /.card-body -->
        <div class="card-footer clearfix">
            <ul class="pagination pagination-sm m-0 float-right">
                <?php if ($npage > 0) { ?>
                    <li class="page-item"><a class="page-link" href="index.php?user&npage=<?php echo $npage-1; ?>">&laquo;</a></li>
                <?php } if (($npage+1) * $nshow < $len_users) { ?>
                    <li class="page-item"><a class="page-link" href="index.php?user&npage=<?php echo $npage+1; ?>">&raquo;</a></li>
                <?php } ?>
            </ul>
        </div>
    </div>
    <!-- /.card -->
</section>
<!-- /.content -->

<?php
include_once('edit_user.php');
include_once('change_pass_user.php');
include_once('delete_user.php');
?>