package Bio::KBase::Loader::LoaderImpl;
use strict;
use Bio::KBase::Exceptions;
# Use Semantic Versioning (2.0.0-rc.1)
# http://semver.org 
our $VERSION = "0.1.0";

=head1 NAME

Loader

=head1 DESCRIPTION

Loader APIs

=cut

#BEGIN_HEADER
#END_HEADER

sub new
{
    my($class, @args) = @_;
    my $self = {
    };
    bless $self, $class;
    #BEGIN_CONSTRUCTOR
    #END_CONSTRUCTOR

    if ($self->can('_init_instance'))
    {
	$self->_init_instance();
    }
    return $self;
}

=head1 METHODS



=head2 mys_example

  $job_id = $obj->mys_example($args)

=over 4

=item Parameter and return types

=begin html

<pre>
$args is a LoaderExampleParams
$job_id is a reference to a list where each element is a string
LoaderExampleParams is a reference to a hash where the following keys are defined:
	ws_id has a value which is a string
	inobj_id has a value which is a string
	outobj_id has a value which is a string
	p_value has a value which is a float
	method has a value which is a string
	num_genes has a value which is an int

</pre>

=end html

=begin text

$args is a LoaderExampleParams
$job_id is a reference to a list where each element is a string
LoaderExampleParams is a reference to a hash where the following keys are defined:
	ws_id has a value which is a string
	inobj_id has a value which is a string
	outobj_id has a value which is a string
	p_value has a value which is a float
	method has a value which is a string
	num_genes has a value which is an int


=end text



=item Description

Description of mys_example: 
Add description here

=back

=cut

sub mys_example
{
    my $self = shift;
    my($args) = @_;

    my @_bad_arguments;
    (ref($args) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument \"args\" (value was \"$args\")");
    if (@_bad_arguments) {
	my $msg = "Invalid arguments passed to mys_example:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
							       method_name => 'mys_example');
    }

    my $ctx = $Bio::KBase::Loader::Service::CallContext;
    my($job_id);
    #BEGIN mys_example
    #END mys_example
    my @_bad_returns;
    (ref($job_id) eq 'ARRAY') or push(@_bad_returns, "Invalid type for return variable \"job_id\" (value was \"$job_id\")");
    if (@_bad_returns) {
	my $msg = "Invalid returns passed to mys_example:\n" . join("", map { "\t$_\n" } @_bad_returns);
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
							       method_name => 'mys_example');
    }
    return($job_id);
}




=head2 version 

  $return = $obj->version()

=over 4

=item Parameter and return types

=begin html

<pre>
$return is a string
</pre>

=end html

=begin text

$return is a string

=end text

=item Description

Return the module version. This is a Semantic Versioning number.

=back

=cut

sub version {
    return $VERSION;
}

=head1 TYPES



=head2 LoaderExampleParams

=over 4



=item Description

num_gene is needed


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
ws_id has a value which is a string
inobj_id has a value which is a string
outobj_id has a value which is a string
p_value has a value which is a float
method has a value which is a string
num_genes has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
ws_id has a value which is a string
inobj_id has a value which is a string
outobj_id has a value which is a string
p_value has a value which is a float
method has a value which is a string
num_genes has a value which is an int


=end text

=back



=cut

1;
