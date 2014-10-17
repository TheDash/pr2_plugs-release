Name:           ros-hydro-pr2-plugs
Version:        1.0.14
Release:        0%{?dist}
Summary:        ROS pr2_plugs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_plugs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-checkerboard-pose-estimation
Requires:       ros-hydro-outlet-pose-estimation
Requires:       ros-hydro-pr2-image-snapshot-recorder
Requires:       ros-hydro-pr2-plugs-actions
Requires:       ros-hydro-pr2-plugs-common
Requires:       ros-hydro-pr2-plugs-msgs
Requires:       ros-hydro-stereo-wall-detection
Requires:       ros-hydro-visual-pose-estimation
BuildRequires:  ros-hydro-catkin

%description
pr2_plugs metapackage. The pr2_plugs metapackage groups all of the functionality
needed for the pr2 to plug itself into the wall

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Oct 17 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.14-0
- Autogenerated by Bloom

* Tue Oct 14 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.13-0
- Autogenerated by Bloom

* Fri Oct 10 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.12-0
- Autogenerated by Bloom

