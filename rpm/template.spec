Name:           ros-hydro-outlet-pose-estimation
Version:        1.0.13
Release:        0%{?dist}
Summary:        ROS outlet_pose_estimation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/outlet_pose_estimation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-opencv2
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-visual-pose-estimation
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-opencv2
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-visual-pose-estimation

%description
outlet_pose_estimation

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
* Tue Oct 14 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.13-0
- Autogenerated by Bloom

* Fri Oct 10 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.12-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.9-0
- Autogenerated by Bloom

* Thu Sep 11 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.8-0
- Autogenerated by Bloom

* Mon Sep 08 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

