Name:           ros-hydro-pr2-plugs-msgs
Version:        1.0.21
Release:        0%{?dist}
Summary:        ROS pr2_plugs_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_plugs_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib-msgs
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs

%description
pr2_plugs_msgs provides the msgs and action definitions required for plugging
in.

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
* Fri Oct 24 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.21-0
- Autogenerated by Bloom

* Fri Oct 24 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.19-0
- Autogenerated by Bloom

* Mon Oct 20 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.17-0
- Autogenerated by Bloom

* Mon Oct 20 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.16-0
- Autogenerated by Bloom

* Fri Oct 17 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.14-0
- Autogenerated by Bloom

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

