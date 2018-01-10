Name:           AuthServer
Version:        1.0.0
Release:        1%{?dist}
Summary:        AuthServer
Group:          Development/Tools
License:        GPL
Source0:        %{name}-%{version}.tar.gz


Requires: npm
Requires: mysql-server
Requires: MySQL-python
Requires: python-setuptools
Requires: python-setuptools-devel


%define  authserverpath /usr/share/
%define  authservice /etc/init.d/


%description
Private cloud disk Auth Server.


%prep
%setup -n %{name}


%install
install -d $RPM_BUILD_ROOT%{authserverpath}
install -d $RPM_BUILD_ROOT%{authservice}
apidoc -i $RPM_BUILD_DIR/%{name} -o $RPM_BUILD_DIR/%{name}/static/
cp -r $RPM_BUILD_DIR/%{name} $RPM_BUILD_ROOT%{authserverpath}
cp $RPM_BUILD_DIR/%{name}/tools/authservice $RPM_BUILD_ROOT%{authservice}
chmod +x $RPM_BUILD_ROOT%{authservice}/authservice



%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}/


%postun
rm -rf /usr/share/%{name}
rm -rf /etc/init.d/authservice

%files
%defattr(-,root,root)
%{authserverpath}
%{authservice}/authservice


%changelog