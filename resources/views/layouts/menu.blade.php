<nav class="mt-2">
    <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
      <!-- Add icons to the links using the .nav-icon class
           with font-awesome or any other icon font library -->
      <li class="nav-item menu-open">
       
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link">
          <i class="nav-icon fas fa-chart-pie"></i>
          <p>
            Tablas
            <i class="right fas fa-angle-left"></i>
          </p>
        </a>
        <ul class="nav nav-treeview">
        
          <li class="nav-item">
            <a href="{{ route('apprentice.index') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Aprendices</p>
            </a>
          </li>
          <li class="nav-item">
            <a href="{{ route('contractor.index') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Contratistas</p>
            </a>
          </li>
          <li class="nav-item">
            <a href="{{ route('plant.index') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Planta</p>
            </a>
          </li>
          <li class="nav-item">
            <a href="{{ route('hours.index') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Organizacion Fechas </p>
            </a>
          </li>          
          <li class="nav-item">
            <a href="{{ route('create.index') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Agregar Ins</p>
            </a>
          </li>
        </ul>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link">
          <i class="nav-icon fas fa-edit"></i>
          <p>
            Correos
            <i class="fas fa-angle-left right"></i>
          </p>
        </a>
        <ul class="nav nav-treeview">
          <li class="nav-item">
            <a href="{{ route('emailone.index') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Primer Correo</p>
            </a>
          </li>
          <li class="nav-item">
            <a href="{{ route('emailone.secondEmail') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Segundo Correo</p>
            </a>
          </li>
          <li class="nav-item">
            <a href="{{ route('emailone.thirdEmail') }}" class="nav-link">
              <i class="far fa-circle nav-icon"></i>
              <p>Tercer Correo</p>
            </a>
          </li>
        </ul>
      </li>
    </ul>
  </nav>