Name:		registry-core-tt-acv
Version:	0.0.5
Release:	1
Summary:	TT ACV linked data registry

License:	apache
URL:		https://github.com/wmo-registers/tt-acv-deploy

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}.tar.gz

Requires:       java-1.7.0-openjdk
Requires:       nginx
Requires:       tomcat7


%description


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
install -D etc/sudoers.d/uklSudoers.conf $RPM_BUILD_ROOT/etc/sudoers.d/uklSudoers.conf
mkdir -p $RPM_BUILD_ROOT/opt/ldregistry/ui
mkdir -p $RPM_BUILD_ROOT/var/opt/ldregistry
mkdir -p $RPM_BUILD_ROOT/var/log/ldregistry
install -D var/lib/tomcat7/webapps/ROOT.war $RPM_BUILD_ROOT/var/lib/tomcat7/webapps/ROOT.war

%pre

service tomcat7 stop
for f in $(find /opt/ldregistry -type f)
do
  owner=$(rpm -qf $f)
  if [ $? -eq 1 ]; then
    rm $f
  fi
done
alternatives --set java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java


%post

service tomcat7 start



%clean
rm -rf $RPM_BUILD_ROOT



%files
/etc/sudoers.d/uklSudoers.conf
%defattr(775,root,tomcat,-)
/var/lib/tomcat7/webapps/ROOT.war
%dir /opt/ldregistry
%dir /opt/ldregistry/ui
%dir /var/opt/ldregistry
%dir /var/log/ldregistry


%changelog
