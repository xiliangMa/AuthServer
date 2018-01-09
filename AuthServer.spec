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


%description
Private cloud disk Auth Server.


%prep
%setup -n %{name}


%install
install -d $RPM_BUILD_ROOT%{authserverpath}
#cp -r $RPM_BUILD_DIR/%{name}-%{version} $RPM_BUILD_ROOT%{authserverpath}
cp -r $RPM_BUILD_DIR/%{name} $RPM_BUILD_ROOT%{authserverpath}


%clean
rm -rf $RPM_BUILD_ROOT
# rm -rf $RPM_BUILD_DIR/%{name}-%{version}/
rm -rf $RPM_BUILD_DIR/%{name}/


%postun
#rm -rf /usr/share/%{name}-%{version}
rm -rf /usr/share/%{name}


%files
%defattr(-,root,root)
%{authserverpath}


%changelog